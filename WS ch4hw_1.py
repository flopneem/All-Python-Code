def draw_square(nm):
    """Takes a turtle (nm), draws a square with it, and then
    moves the turtle to the right."""
    for dummy in range(4):
        nm.forward(20)
        nm.left(90)

    nm.penup()
    nm.forward(40)
    nm.pendown()

import turtle 

alex = turtle.Turtle()
alex.color("HotPink")
alex.pensize(3)
wn = turtle.Screen()
wn.bgcolor("lightgreen")

for dummy in range(5):
    draw_square(alex)

wn.mainloop()
