import turtle
wn = turtle.Screen()
t = turtle.Turtle()

t.penup()
t.forward(200)
t.pendown()
t.left(90)
t.forward(200)
t.backward(400)
t.left(90)

for i in range(3):
    t.forward(400)
    t.right(90)
