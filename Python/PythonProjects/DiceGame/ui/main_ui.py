# ui/main_ui.py
# Tkinter UI for Dice Tournament Game

import os
import sys
import time
import threading
import tkinter as tk
from tkinter import ttk, messagebox

from logic.game_engine import GameEngine, Player

# ---------- Optional sound (Windows winsound) ----------
try:
    import winsound
    HAS_SOUND = True
except ImportError:
    HAS_SOUND = False


ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
TOTAL_ROUNDS = 3


def _asset_path(filename: str) -> str:
    return os.path.join(ASSETS_DIR, filename)


class DiceTournamentApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Dice Tournament Game")
        self.root.configure(bg="#111111")

        # Window size
        self.root.geometry("900x550")

        # Game engine instance (created after setup)
        self.game = None

        # Dice images dict: {1: PhotoImage, ..., 6: PhotoImage}
        self.dice_images = {}
        self._load_dice_images()

        # Sound config
        self.sound_on = True
        self.roll_sound_path = _asset_path("roll.mp3")

        # UI state
        self.current_roll_animating = False

        # Frames
        self.setup_mode_frame()
        self.setup_game_frame()

        # Show mode frame first
        self.mode_frame.tkraise()

    # ---------- Assets ----------

    def _load_dice_images(self):
        """Load dice1.png .. dice6.png from assets folder."""
        for i in range(1, 7):
            path = _asset_path(f"dice{i}.png")
            try:
                img = tk.PhotoImage(file=path)
            except Exception:
                # Fallback blank 50x50 if missing
                img = tk.PhotoImage(width=64, height=64)
            self.dice_images[i] = img

    def play_roll_sound(self):
        if self.sound_on and HAS_SOUND and os.path.exists(self.roll_sound_path):
            threading.Thread(
                target=winsound.PlaySound,
                args=(self.roll_sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC),
                daemon=True
            ).start()

    # ---------- Mode Selection UI ----------

    def setup_mode_frame(self):
        self.mode_frame = tk.Frame(self.root, bg="#111111")
        self.mode_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        title = tk.Label(
            self.mode_frame,
            text="DICE TOURNAMENT",
            font=("Arial", 24, "bold"),
            fg="#FF5555",
            bg="#111111"
        )
        title.pack(pady=20)

        mode_label = tk.Label(
            self.mode_frame,
            text="Choose Game Mode",
            font=("Arial", 14),
            fg="white",
            bg="#111111"
        )
        mode_label.pack(pady=10)

        self.mode_var = tk.StringVar(value="pvc")

        pvc_radio = tk.Radiobutton(
            self.mode_frame, text="Player vs Computer",
            variable=self.mode_var, value="pvc",
            font=("Arial", 12), fg="white",
            bg="#111111", selectcolor="#222222"
        )
        pvc_radio.pack(pady=5)

        multi_radio = tk.Radiobutton(
            self.mode_frame, text="Multiplayer (2 - 4 players)",
            variable=self.mode_var, value="multi",
            font=("Arial", 12), fg="white",
            bg="#111111", selectcolor="#222222"
        )
        multi_radio.pack(pady=5)

        # Player name inputs
        self.name_entries = []
        names_frame = tk.Frame(self.mode_frame, bg="#111111")
        names_frame.pack(pady=20)

        tk.Label(
            names_frame,
            text="Enter Player Names:",
            font=("Arial", 12),
            fg="white",
            bg="#111111"
        ).grid(row=0, column=0, columnspan=2, pady=(0, 5), sticky="w")

        for i in range(4):
            tk.Label(
                names_frame,
                text=f"Player {i+1}:",
                font=("Arial", 10),
                fg="white",
                bg="#111111"
            ).grid(row=i+1, column=0, sticky="e", padx=5, pady=3)
            e = tk.Entry(names_frame, width=20)
            e.grid(row=i+1, column=1, padx=5, pady=3)
            self.name_entries.append(e)

        # Info note
        note = tk.Label(
            self.mode_frame,
            text="Note:\n• For Player vs Computer, only Player 1 name is used.\n• For Multiplayer, fill 2 to 4 names.",
            font=("Arial", 10),
            fg="#AAAAAA",
            bg="#111111",
            justify="left"
        )
        note.pack(pady=5)

        start_button = tk.Button(
            self.mode_frame,
            text="Start Game",
            font=("Arial", 12, "bold"),
            bg="#FF5555", fg="white",
            command=self.start_game_from_mode
        )
        start_button.pack(pady=10)

    def start_game_from_mode(self):
        mode = self.mode_var.get()

        if mode == "pvc":
            name = self.name_entries[0].get().strip() or "Player"
            players = [
                Player(name=name, is_computer=False),
                Player(name="Computer", is_computer=True)
            ]
        else:
            # Multiplayer
            names = [e.get().strip() for e in self.name_entries]
            names = [n for n in names if n]  # remove blanks
            if len(names) < 2:
                messagebox.showwarning("Input Error", "Enter at least 2 player names.")
                return
            if len(names) > 4:
                names = names[:4]
            players = [Player(name=n) for n in names]

        self.game = GameEngine(players, total_rounds=TOTAL_ROUNDS)
        self.setup_scoreboard()
        self.update_turn_info()
        self.game_frame.tkraise()

    # ---------- Game UI ----------

    def setup_game_frame(self):
        self.game_frame = tk.Frame(self.root, bg="#111111")
        self.game_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Top area: title + round info + sound toggle
        top_frame = tk.Frame(self.game_frame, bg="#111111")
        top_frame.pack(fill="x", pady=10)

        title = tk.Label(
            top_frame,
            text="DICE TOURNAMENT",
            font=("Arial", 20, "bold"),
            fg="#FF5555", bg="#111111"
        )
        title.pack(side="left", padx=20)

        self.round_label = tk.Label(
            top_frame,
            text="Round: 1 / 3",
            font=("Arial", 12),
            fg="white", bg="#111111"
        )
        self.round_label.pack(side="left", padx=20)

        # Sound toggle button
        self.sound_button = tk.Button(
            top_frame,
            text="Sound: ON",
            font=("Arial", 10, "bold"),
            bg="#444444", fg="white",
            command=self.toggle_sound
        )
        self.sound_button.pack(side="right", padx=20)

        # Middle layout: left = dice + info, right = scoreboard
        middle_frame = tk.Frame(self.game_frame, bg="#111111")
        middle_frame.pack(fill="both", expand=True, padx=20, pady=10)

        left_frame = tk.Frame(middle_frame, bg="#111111")
        left_frame.pack(side="left", fill="both", expand=True, padx=10)

        right_frame = tk.Frame(middle_frame, bg="#222222", bd=2, relief="sunken")
        right_frame.pack(side="right", fill="y", padx=10)

        # Dice display
        self.dice_label = tk.Label(
            left_frame,
            image=None,
            bg="#111111"
        )
        self.dice_label.pack(pady=20)

        # Turn info
        self.turn_label = tk.Label(
            left_frame,
            text="",
            font=("Arial", 14, "bold"),
            fg="#FFFFFF", bg="#111111"
        )
        self.turn_label.pack(pady=5)

        self.rolls_label = tk.Label(
            left_frame,
            text="Rolls: ",
            font=("Arial", 12),
            fg="#DDDDDD", bg="#111111"
        )
        self.rolls_label.pack(pady=5)

        # Roll button
        self.roll_button = tk.Button(
            left_frame,
            text="ROLL DICE",
            font=("Arial", 14, "bold"),
            bg="#FF5555", fg="white",
            width=12,
            command=self.on_roll_click
        )
        self.roll_button.pack(pady=20)

        # Next turn button
        self.next_button = tk.Button(
            left_frame,
            text="Next Player / Round",
            font=("Arial", 11),
            bg="#444444", fg="white",
            command=self.on_next_click,
            state="disabled"
        )
        self.next_button.pack(pady=5)

        # Scoreboard (right side)
        tk.Label(
            right_frame,
            text="Scoreboard",
            font=("Arial", 14, "bold"),
            fg="#FFDD55", bg="#222222"
        ).pack(pady=10)

        self.score_tree = ttk.Treeview(
            right_frame,
            columns=("score",),
            show="headings",
            height=8
        )
        self.score_tree.heading("score", text="Score")
        self.score_tree.column("score", width=80, anchor="center")
        self.score_tree.pack(pady=5, padx=5, fill="y")

        style = ttk.Style()
        style.configure("Treeview", background="#222222", fieldbackground="#222222", foreground="white")
        style.map("Treeview", background=[("selected", "#444444")])

        # Bottom frame: info/winner
        bottom_frame = tk.Frame(self.game_frame, bg="#111111")
        bottom_frame.pack(fill="x", pady=10)

        self.status_label = tk.Label(
            bottom_frame,
            text="",
            font=("Arial", 11),
            fg="#DDDDDD", bg="#111111"
        )
        self.status_label.pack(side="left", padx=20)

        self.restart_button = tk.Button(
            bottom_frame,
            text="Restart Game",
            font=("Arial", 10),
            bg="#555555", fg="white",
            command=self.restart_game
        )
        self.restart_button.pack(side="right", padx=20)

    def setup_scoreboard(self):
        """Fill scoreboard with players."""
        for row in self.score_tree.get_children():
            self.score_tree.delete(row)

        if not self.game:
            return

        for p in self.game.players:
            self.score_tree.insert("", tk.END, iid=p.name, values=(p.score,))
            self.score_tree.set(p.name, column="score", value=p.score)
            self.score_tree.item(p.name, text=p.name)

        # Show player names as '#' column through tag simulation
        self.score_tree["displaycolumns"] = ("score",)
        self.score_tree.heading("#0", text="Player")
        self.score_tree.column("#0", width=120, anchor="w")

        for p in self.game.players:
            self.score_tree.item(p.name, text=p.name)

    def update_scoreboard(self):
        if not self.game:
            return
        for p in self.game.players:
            self.score_tree.set(p.name, column="score", value=p.score)

    def toggle_sound(self):
        self.sound_on = not self.sound_on
        self.sound_button.config(text=f"Sound: {'ON' if self.sound_on else 'OFF'}")

    def update_turn_info(self):
        if not self.game:
            return

        player = self.game.get_current_player()
        self.round_label.config(text=f"Round: {self.game.current_round} / {self.game.total_rounds}")
        self.turn_label.config(text=f"Turn: {player.name}")
        self.rolls_label.config(text="Rolls: ")
        self.status_label.config(text="Roll the dice!")
        self.roll_button.config(state="normal")
        self.next_button.config(state="disabled")

        # Set default dice image (1)
        self.dice_label.config(image=self.dice_images.get(1))

    def animate_dice(self, callback):
        """Simple dice spin animation before showing actual result."""
        self.current_roll_animating = True

        def _spin(count=0):
            if count >= 10:
                self.current_roll_animating = False
                callback()
                return
            import random
            temp_value = random.randint(1, 6)
            self.dice_label.config(image=self.dice_images.get(temp_value))
            self.root.after(70, _spin, count + 1)

        self.play_roll_sound()
        _spin()

    def on_roll_click(self):
        if not self.game or self.current_roll_animating:
            return

        player = self.game.get_current_player()
        self.roll_button.config(state="disabled")
        self.status_label.config(text=f"{player.name} is rolling...")

        def after_animation():
            rolls, turn_score = self.game.roll_turn()
            self.dice_label.config(image=self.dice_images.get(rolls[-1]))
            self.rolls_label.config(text=f"Rolls: {rolls}  | Turn Score: {turn_score}")
            self.update_scoreboard()
            self.status_label.config(text=f"{player.name} scored {turn_score} this turn.")
            self.next_button.config(state="normal")

        self.animate_dice(after_animation)

    def on_next_click(self):
        if not self.game:
            return

        if self.game.is_game_over():
            # Show winner(s)
            winners = self.game.get_winners()
            names = ", ".join(p.name for p in winners)
            max_score = winners[0].score
            msg = f"Game Over!\nWinner(s): {names}\nScore: {max_score}"
            self.status_label.config(text=msg)
            messagebox.showinfo("Result", msg)
            self.roll_button.config(state="disabled")
            self.next_button.config(state="disabled")
            return

        self.game.next_player()
        if self.game.is_game_over():
            self.on_next_click()  # re-check
        else:
            self.update_turn_info()

    def restart_game(self):
        if not self.game:
            return
        self.game.reset()
        self.setup_scoreboard()
        self.update_turn_info()
        self.status_label.config(text="Game restarted.")

# ---------- Public function to run app ----------

def run_app():
    root = tk.Tk()
    app = DiceTournamentApp(root)
    root.mainloop()
