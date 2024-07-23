import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
    size = simpledialog.askinteger(title="Give me the radius of any value in pixels", prompt="n/a")
    # Make a new turtle
    bug = turtle.Turtle()
    bug.shape('turtle')
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    bug.circle(size)
    # Call the turtle .penup() method
    bug.penup()
    # Move your turtle to a new x,y position using .goto()
    bug.goto(0, 0)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    area = size * 3.14 ^ 2
    # Write the area of your circle using the turtle .write() method
    # my_turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
    bug.write(arg="area = " + str(area), move=True, align='left', font=('Arial' ,8, 'normal'))
    # Hide your turtle
    bug.hideturtle()
    # Call turtle.done()
    bug.done()
# ======================================================================================================
# Help with calculate area of circle and store it in variable
# ======================================================================================================
