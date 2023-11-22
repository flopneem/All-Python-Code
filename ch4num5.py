##https://youtu.be/zCCI8btpqCI




import turtle
t = turtle.Turtle

def spiraltime(t, angle):
    length = 1
    for i in range(84):
        t.forward(length)
        t.right(angle)
        length = length + 2


wn = turtle.Screen()
wn.bgcolor('lightgreen')

buddyboi = turtle.Turtle
buddyboi.color = ('blue')

buddyboi.penup()
buddyboi.backward(110)
buddyboi.pendown()

drawSpiral(buddyboi, 90)

buddyboi.home()
buddyboi.penup()
buddyboi.foward(90)
buddyboi.pendown()

spiraltime(buddyboi, 89)

