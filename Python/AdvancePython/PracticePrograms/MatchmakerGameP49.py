# Program: Match making Game

import random
import time
import tkinter as tk
from tkinter import Tk, Button, DISABLED, font


def show_symbol(x, y):
    global first
    global previousX, previousY

    # Ignore clicks on already-matched or already-flipped buttons
    if buttons[x, y]['state'] == DISABLED:
        return
    if not first and previousX == x and previousY == y:
        return

    buttons[x, y]['text'] = button_symbols[x, y]
    buttons[x, y].update_idletasks()

    if first:
        previousX = x
        previousY = y
        first = False
    else:
        if buttons[previousX, previousY]['text'] != buttons[x, y]['text']:
            root.after(500, hide_symbols, x, y)
        else:
            buttons[previousX, previousY].config(state=DISABLED, relief='sunken',
                                                  bg='#d4edda', disabledforeground='#2e7d32')
            buttons[x, y].config(state=DISABLED, relief='sunken',
                                  bg='#d4edda', disabledforeground='#2e7d32')
        first = True


def hide_symbols(x, y):
    buttons[previousX, previousY]['text'] = ''
    buttons[x, y]['text'] = ''


root = Tk()
root.title('Matchmaker')
root.resizable(width=False, height=False)
root.configure(bg='#e8e8e8')

# Padding around the grid
frame = tk.Frame(root, bg='#e8e8e8', padx=12, pady=12)
frame.pack()

buttons = {}
first = True
previousX = 0
previousY = 0
button_symbols = {}

symbols = [
    u'\u2702', u'\u2702',  # ✂
    u'\u2705', u'\u2705',  # ✅
    u'\u2708', u'\u2708',  # ✈
    u'\u2709', u'\u2709',  # ✉
    u'\u270A', u'\u270A',  # ✊
    u'\u270B', u'\u270B',  # ✋
    u'\u270C', u'\u270C',  # ✌
    u'\u270F', u'\u270F',  # ✏
    u'\u2712', u'\u2712',  # ✒
    u'\u2714', u'\u2714',  # ✔
    u'\u2716', u'\u2716',  # ✖
    u'\u2728', u'\u2728',  # ✨
]

random.shuffle(symbols)

# Use a font that renders emoji/symbols well
try:
    btn_font = font.Font(family='Segoe UI Emoji', size=16)
except Exception:
    btn_font = font.Font(family='TkDefaultFont', size=14)

for x in range(6):
    for y in range(4):
        btn = Button(
            frame,
            text='',
            command=lambda bx=x, by=y: show_symbol(bx, by),
            width=5,
            height=2,
            font=btn_font,
            bg='#f0f0f0',
            activebackground='#dcdcdc',
            relief='raised',
            bd=2,
            cursor='hand2',
        )
        btn.grid(column=x, row=y, padx=4, pady=4)
        buttons[x, y] = btn
        button_symbols[x, y] = symbols.pop()

root.mainloop()