def draw_poly(t, n, sz):
    """Make a turtle t draw a polygon with n sides of length sz."""

    for dummy in range(n):
        t.forward(sz)
        t.left(360 / n)

import turtle

tess = turtle.Turtle()          # Create a turtle and set some attributes.
tess.color("HotPink")
tess.pensize(3)

wn = turtle.Screen()            # Create a screen and set its color.
wn.bgcolor("lightgreen")

draw_poly(tess, 8, 50)          # Draw the polygon

wn.mainloop()                   # Keep the window open till user closes it.
