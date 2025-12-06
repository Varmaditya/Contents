# Personal Notebook/ REMINDER APP  (UI)
import tkinter as tk
from tkinter import messagebox, ttk
import datetime
import os

# ----------------- CONFIG -----------------
NOTES_FILE = "notes.txt"

# UI COLORS (Same as Food App)
COLOR_BG = "#F7E396"
COLOR_ACCENT = "#E97F4A"
COLOR_PRIMARY = "#434E78"
COLOR_SECONDARY = "#607B8F"
COLOR_WHITE = "#FFFFFF"


# ----------------- FILE HANDLING -----------------

def load_notes():
    """Load notes from file into a list of dicts."""
    notes = []
    if not os.path.exists(NOTES_FILE):
        return notes

    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]

    i = 0
    while i < len(lines):
        if lines[i].strip() == "----- NOTE -----":
            date_line = lines[i + 1] if i + 1 < len(lines) else ""
            msg_line = lines[i + 2] if i + 2 < len(lines) else ""
            i += 4

            if date_line.startswith("Date:") and msg_line.startswith("Message:"):
                date_text = date_line.replace("Date:", "", 1).strip()
                message_text = msg_line.replace("Message:", "", 1).strip()
                notes.append({"date": date_text, "message": message_text})
        else:
            i += 1

    return notes


def save_notes(notes):
    """Save notes in block format."""
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        for note in notes:
            f.write("----- NOTE -----\n")
            f.write(f"Date: {note['date']}\n")
            f.write(f"Message: {note['message']}\n")
            f.write("-----------------\n")


# ----------------- LOGIC FUNCTIONS -----------------

def refresh_list():
    note_list.delete(*note_list.get_children())
    for idx, note in enumerate(notes, 1):
        note_list.insert("", "end", values=(idx, note["date"], note["message"]))


def add_note():
    text = note_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Empty", "Note cannot be empty.")
        return

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    notes.append({"date": now, "message": text})
    save_notes(notes)
    refresh_list()
    note_entry.delete("1.0", tk.END)
    messagebox.showinfo("Added", "Note added successfully.")


def delete_note():
    selected = note_list.selection()
    if not selected:
        messagebox.showwarning("Select", "Select a note to delete.")
        return

    index = int(note_list.item(selected, "values")[0]) - 1
    confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this note?")
    if confirm:
        notes.pop(index)
        save_notes(notes)
        refresh_list()


def edit_note():
    selected = note_list.selection()
    if not selected:
        messagebox.showwarning("Select", "Select a note to update.")
        return

    index = int(note_list.item(selected, "values")[0]) - 1
    old_note = notes[index]["message"]

    # Pop-up Window for update
    update_win = tk.Toplevel(root)
    update_win.title("Update Note")
    update_win.config(bg=COLOR_BG)
    update_win.geometry("350x250")

    tk.Label(update_win, text="Edit Note:", font=("Poppins", 12, "bold"), bg=COLOR_BG, fg=COLOR_PRIMARY).pack(pady=5)
    txt = tk.Text(update_win, font=("Poppins", 10), height=8, width=35)
    txt.pack(padx=10, pady=5)
    txt.insert(tk.END, old_note)

    def save_edit():
        new_text = txt.get("1.0", tk.END).strip()
        if not new_text:
            messagebox.showwarning("Empty", "Updated text cannot be empty.")
            return
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        notes[index] = {"date": now, "message": new_text}
        save_notes(notes)
        refresh_list()
        update_win.destroy()
        messagebox.showinfo("Updated", "Note updated successfully!")

    tk.Button(update_win, text="Save Update", bg=COLOR_PRIMARY, fg="white",
              font=("Poppins", 10, "bold"), relief="flat", padx=10, pady=5,
              command=save_edit).pack(pady=10)


def search_notes():
    keyword = search_box.get().strip().lower()
    if not keyword:
        messagebox.showwarning("Empty", "Enter keyword to search.")
        return

    filtered = []
    for idx, note in enumerate(notes, 1):
        if keyword in note["message"].lower() or keyword in note["date"]:
            filtered.append((idx, note))

    if not filtered:
        messagebox.showinfo("No Match", "No notes matched your search.")
        return

    note_list.delete(*note_list.get_children())
    for serial, note in filtered:
        note_list.insert("", "end", values=(serial, note["date"], note["message"]))


# ----------------- UI SETUP -----------------

root = tk.Tk()
root.title("📒 Personal Notebook / Reminder")
root.geometry("900x500")
root.config(bg=COLOR_BG)

# Rounded Button Helper
def rbutton(parent, text, cmd, bg):
    return tk.Button(parent, text=text, command=cmd,
        bg=bg, fg="white", activebackground=bg,
        font=("Poppins", 10, "bold"),
        relief="flat", padx=10, pady=6)

# Title
tk.Label(root, text="📘 Personal Notebook / Reminder", font=("Poppins", 20, "bold"),
         bg=COLOR_BG, fg=COLOR_PRIMARY).pack(pady=10)

# Main Frame
main = tk.Frame(root, bg=COLOR_BG)
main.pack(fill="both", expand=True, padx=10)

# -------- Left Panel (Add Note) --------
left = tk.Frame(main, bg=COLOR_BG)
left.pack(side="left", fill="y", padx=10, pady=10)

tk.Label(left, text="📝 Write a New Note", font=("Poppins", 12, "bold"),
         bg=COLOR_BG, fg=COLOR_PRIMARY).pack(anchor="w")

note_entry = tk.Text(left, width=40, height=7, font=("Poppins", 10))
note_entry.pack(pady=5)

rbutton(left, "➕ Add Note", add_note, COLOR_ACCENT).pack(fill="x", pady=5)

tk.Label(left, text="🔍 Search Notes", font=("Poppins", 12, "bold"),
         bg=COLOR_BG, fg=COLOR_PRIMARY).pack(anchor="w", pady=(15,0))
search_box = tk.Entry(left, font=("Poppins", 10))
search_box.pack(fill="x", pady=3)
rbutton(left, "🔎 Search", search_notes, COLOR_SECONDARY).pack(fill="x")

# -------- Right Panel (Note List) --------
right = tk.Frame(main, bg=COLOR_WHITE, bd=3, relief="ridge")
right.pack(side="left", fill="both", expand=True, padx=10, pady=5)

tk.Label(right, text="📒 Saved Notes", font=("Poppins", 13, "bold"),
         bg=COLOR_WHITE, fg=COLOR_PRIMARY).pack(anchor="w", padx=5, pady=5)

columns = ("No.", "Date", "Message")
note_list = ttk.Treeview(right, columns=columns, show="headings", height=15)
for col in columns:
    note_list.heading(col, text=col)
    note_list.column(col, width=150 if col != "Message" else 400)

note_list.pack(fill="both", expand=True)

# Buttons below table
btn_frame = tk.Frame(right, bg=COLOR_WHITE)
btn_frame.pack(fill="x", pady=5)

rbutton(btn_frame, "✏️ Edit", edit_note, COLOR_SECONDARY).pack(side="left", padx=5)
rbutton(btn_frame, "🗑 Delete", delete_note, "#CC4A4A").pack(side="left", padx=5)
rbutton(btn_frame, "🔄 Show All", refresh_list, COLOR_PRIMARY).pack(side="right", padx=5)

# ------------ Load existing notes ------------
notes = load_notes()
refresh_list()

root.mainloop()
