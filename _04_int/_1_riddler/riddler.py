from tkinter import *
import tkinter as tk
import math
import turtle, sys
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
#"""
# Write a python program that asks the user a minimum of 3 riddles.

# You can look at riddles.com if you don't already know any riddles.

# Collect the response of each riddle from the user and compare their
#  answers to the correct answer.

# Use a variable to keep track of the correctly answered riddles

# After all the riddles have been asked, tell the user how many they got
#  correct
#"""
    score = 0
    name = simpledialog.askstring(title="What is your name.",prompt="!@#$%^&*()_+")
    if name == "Jude" or name == "bradley" or name == "jude" or name == "Bradley" or name == "jude bradley" or name == "Jude Bradley" or name == "Gerry" or name == "Jerry" or name == "Gerardo" or name == "Gerardo Montana" or name == "Gerry Montana":
        simpledialog.askinteger(title="DIE", prompt="I AM GOING TO SNAP YOUR NECK, BREAK ALL OF YOUR BONES, AND DONATE YOUR ORGANS TO CHARITY")
        messagebox.askquestion(title="sample", message="none")
        messagebox.showwarning(title="Alert", message="Motion detected at the front door")
        sys.exit(0)
    else:
        window.withdraw()
    a = simpledialog.askstring(title="YOU WILL DIE.", prompt="YOU ARE HOMELESS.\n"
    "YOU NEED TO GET YOUR JOB BACK AND YOUR HOME.\n"
    "What should you do first?\n"
    "A. Study\n"
    "B. Survive\n"
    "C. Find shelter")

    if a == "b" or a == "B":
        simpledialog.askstring(title="correct.",prompt="I point for you... im getting stabbed in the back as im writing thi")
        score += 1
    else:
        simpledialog.askstring(title="Die.", prompt="")

    b = simpledialog.askinteger(title="Shark", prompt="What should you do when you encounter a shark.\n"
    "1. Get away from it as fast as possible \n"
    "2. Stand still until it goes away\n"
    "3. Fight back\n"
    "4. Move past it")
    if b == 1:
        simpledialog.askstring(title="ARE YOU CRAZY?!", prompt="ARE YOU CRAZY?!")
        sys.exit(0)
    if b == 2 or b == 4:
        simpledialog.askstring(title="Partially correct", prompt="Eh, it could be better")
    if b == 3:
        simpledialog.askstring(title="The best option", prompt="The primary targets when hitting a shark are: Gills, eyes, nose (Nose is more risky because of mouth)")
        score += 1
    KILL = simpledialog.askstring(title="No.", prompt="No more")
    if KILL == "games" or KILL == "game" or KILL == "screen" or KILL == "screentime" or KILL == "technology":
        score += 1
        simpledialog.askstring(title="point.", prompt= score )
    else:
        simpledialog.askstring(title="n/a", prompt= score )
