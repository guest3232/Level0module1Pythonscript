from tkinter import *
import tkinter as tk
import math
import turtle
from tkinter import messagebox, simpledialog, Tk
"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
if __name__ == '__main__':
    turtl = turtle.Turtle()
    choose = simpledialog.askstring(title="Choose", prompt="add, subtract, multiply, divide.")
    die = simpledialog.askinteger(title="DIE...", prompt="give me a specific number")
    kill = simpledialog.askinteger(title="KILL YOURSELF", prompt="or give me a specific number")
    if choose == "add" or choose == "a":
        turtl.write(arg=int(die) + int(kill), move=True, align='left')
    elif choose == "subtract" or choose == "s":
        turtl.write(arg=int(die) - int(kill), move=True, align='right')
    elif choose == "multiply" or choose == "m":
        turtl.write(arg=int(die) * int(kill), move=True, align="left")
    elif choose == "divide" or choose == "d":
        turtl.write(arg=int(die) / int(kill), move=True, align="right")
    turtl.hideturtle()
    turtle.done()
