# Program: Modern Music Player

import tkinter as tk
from tkinter import filedialog
import pygame

pygame.mixer.init()

class MusicPlayer:

    def __init__(self, root):
        self.root = root
        self.root.title("🎵 Neon Music Player")
        self.root.geometry("500x400")
        self.root.config(bg="#121212")
        self.current_song = ""

        # ---------------- TITLE ----------------
        title = tk.Label(
            root,
            text="🎵 MUSIC PLAYER",
            font=("Roboto", 24, "bold"),
            bg="#121212",
            fg="#00ffff"
        )

        title.pack(pady=20)

        # ---------------- SONG LABEL ----------------
        self.song_label = tk.Label(
            root,
            text="No song selected",
            font=("Arial", 14),
            bg="#121212",
            fg="white"
        )

        self.song_label.pack(pady=20)

        # ---------------- BUTTON FRAME ----------------
        frame = tk.Frame(root, bg="#121212")
        frame.pack(pady=20)

        # ---------------- BUTTONS ----------------
        open_btn = tk.Button(
            frame,
            text="📂 Open",
            command=self.load_song,
            bg="#00ffff",
            fg="black",
            font=("Arial", 12, "bold"),
            padx=20
        )

        open_btn.grid(row=0, column=0, padx=10)
        play_btn = tk.Button(
            frame,
            text="▶ Play",
            command=self.play_song,
            bg="#39ff14",
            fg="black",
            font=("Arial", 12, "bold"),
            padx=20
        )

        play_btn.grid(row=0, column=1, padx=10)
        stop_btn = tk.Button(
            frame,
            text="⏹ Stop",
            command=self.stop_song,
            bg="#ff0055",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=20
        )

        stop_btn.grid(row=0, column=2, padx=10)

    # ---------------- LOAD SONG ----------------
    def load_song(self):
        self.current_song = filedialog.askopenfilename()

        if self.current_song:
            self.song_label.config(
                text=self.current_song.split("/")[-1]
            )

    # ---------------- PLAY SONG ----------------
    def play_song(self):

        if self.current_song:
            pygame.mixer.music.load(self.current_song)

            pygame.mixer.music.play()

    # ---------------- STOP SONG ----------------

    def stop_song(self):
        pygame.mixer.music.stop()


root = tk.Tk()
app = MusicPlayer(root)
root.mainloop()