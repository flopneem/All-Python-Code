import turtle
wn=turtle.Screen()
def draw_square(t,sz):
    for x in range(6):
        t.forward(sz)
        t.left(60)
alex=turtle.Turtle()
draw_square(alex,150)
