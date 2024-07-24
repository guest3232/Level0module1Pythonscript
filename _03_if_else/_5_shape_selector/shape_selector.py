import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    #DONT
    # Make a new turtle
    HELP = turtle.Turtle()
    HELP.shape('turtle')
    # Ask the user what shape they want to draw and store it in a variable
    b = simpledialog.askstring(title="Don't", prompt="L:AKSDJ:LASDJK:LASKDJL:ADSJL:DASJL:ASDJ:LSDJKLA:DJAL:SDJ:LASDJK:LASKJFDna;klgj;laejrpahoptrjaop\n"
    "A. Circle\n"
    "B. Triangle\n"
    "C. Square\n"
    "D. Pentagon\n"
    "E. Hexagon\n"
    "F. Heptagon\n"
    "G. Octogon\n"
    "H. ???\n"
    "I. ??? (Yeah i don't know my shapes. im stupid like a dead person")
    # Draw the shape requested by the user using if-elif-else statements
    HELP.pendown()
    if b == "a" or b == "A":
        HELP.circle(radius=100, steps=100)
    elif b == "b" or b == "B":
        for turn in range(3):
            HELP.forward(100)
            HELP.left(120)
    elif b == "c" or b == "C":
        for turn in range(4):
            HELP.forward(100)
            HELP.left(90)
    elif b == "d" or b == "D":
        for turn in range(5):
            HELP.forward(100)
            HELP.left(360/5) #72
    elif b == "e" or b == "E":
        for turn in range(6):
            HELP.forward(100)
            HELP.left(60)
    elif b == "f" or b == "F":
        for turn in range(7):
            HELP.forward(100)
            HELP.left(360/7) #50
    elif b == "g" or b == "G":
        for turn in range(8):
            HELP.forward(100)
            HELP.left(360/8) #42.5
    elif b == "h" or b == "H":
        for turn in range(9):
            HELP.forward(100)
            HELP.left(360/9) #40
    elif b == "i" or b == "I":
        for turn in range(10):
            HELP.forward(100)
            HELP.left(36)
    else:
        HELP.write(arg="HELPMEHELPMEHELPMEHELPMEHELPMEHELPMEHELPMEHELPME", move=True, align='left', font=('Arial' ,8, 'normal'))
        HELP.hideturtle()
    # Call the turtle .done() method
    turtle.done()
