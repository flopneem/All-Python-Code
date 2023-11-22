##https://youtu.be/WMT5QTGEoXA (Part 1)
##https://youtu.be/0TFQjJFU2Kk (Part 2)


import turtle
t = turtle.Pen()
t.shape('turtle')
t.color('blue')
t.stamp()
move = 30

for i in range(12):
    t.penup()
    t.forward(50)
    t.pendown()
    t.forward(25)
    t.penup()
    t.forward(15)
    t.stamp()
    t.home()
    t.right(move)
    move = move + 30
