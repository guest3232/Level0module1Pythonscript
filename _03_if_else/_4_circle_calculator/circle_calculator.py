from tkinter import *
import tkinter as tk
import math
import turtle
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':

    myTurtle = turtle.Turtle()
    myTurtle.shape('turtle')
# Write a Python program that asks the user for the radius of a circle.
    c = simpledialog.askinteger(title="Radius of a circle", prompt='')
    d = simpledialog.askstring(title='Choose: Area or Circumference', prompt="A. area\n"
    "B. circumference")

#    area = math.pi * c * c
#    circumference = math.pi * c * 2

#STOP
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

    myTurtle.circle(c)
    myTurtle.pendown()
    myTurtle.goto(0, 0)
    a = math.pi
    if d == 'area':
        myTurtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial' ,8, 'normal'))

    elif d == 'circumference':
        turtle.write(arg="circumference = " + str(circumference), move=True, align='left', font=('Arial' ,8, 'normal'))
    turtle.hideturtle()
    # Call turtle.done()
    turtle.done()

#Area = πr^2
#Circumference = 2πr
