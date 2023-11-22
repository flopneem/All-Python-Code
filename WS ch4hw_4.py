def draw_poly(t, n, sz):
    """Makes turtle t draw an n-sided polygon with each side of
       length sz."""

    for dummy in range(n):
        t.forward(sz)
        t.left(360 / n)

import turtle

tess = turtle.Turtle()     # Set up a turtle and attributes.
tess.color("blue")
tess.pensize(2)

wn = turtle.Screen()       # Set up screen for it draw on
wn.bgcolor("lightgreen")   # and some attributes.
wn.title("Pretty pattern")

for dummy in range(0, 20):   # Draws a series of squares, 
    draw_poly(tess, 4, 100)  
    tess.right(18)           # and rotates to match pattern.

wn.mainloop()                # Hold window open.
