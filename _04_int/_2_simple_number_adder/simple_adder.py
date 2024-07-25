from tkinter import *
import tkinter as tk
import math
import turtle
from tkinter import messagebox, simpledialog, Tk
"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
if __name__ == '__main__':
    window = Tk()
    turtl = turtle.Turtle()
    die = simpledialog.askinteger(title="DIE...", prompt="give me a specific number")
    kill = simpledialog.askinteger(title="KILL YOURSELF", prompt="or give me a specific number")
    turtl.write(arg=int(die) + int(kill), move=True, align='left')
    turtl.hideturtle()
    turtle.done()
