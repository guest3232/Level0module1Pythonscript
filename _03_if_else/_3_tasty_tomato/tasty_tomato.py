from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk

window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices
c = simpledialog.askstring(title="Color of a tomato", prompt="(no capitals, no numbers)")

# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato
if c == 'red':
    canvas.create_oval(75, 200, 400, 450, fill="red", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="red", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
elif c == 'orange':
    canvas.create_oval(75, 200, 400, 450, fill="orange", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="orange", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
elif c == 'yellow':
    canvas.create_oval(75, 200, 400, 450, fill="yellow", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="yellow", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
elif c == 'green':
    canvas.create_oval(75, 200, 400, 450, fill="green", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="green", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="brown", outline="")
elif c == 'blue':
    canvas.create_oval(75, 200, 400, 450, fill="blue", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="blue", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
elif c == 'purple':
    canvas.create_oval(75, 200, 400, 450, fill="purple", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="purple", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
elif c == 'pink':
    canvas.create_oval(75, 200, 400, 450, fill="pink", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="pink", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
root.mainloop()
