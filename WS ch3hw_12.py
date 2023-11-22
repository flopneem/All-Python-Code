import turtle
tess=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor('lightgreen')
tess=turtle.Pen()
tess.shape('turtle')
tess.color('red')
tess.stamp()
turn= 30
for i in range(12):
    tess.penup()
    tess.fd(50)
    tess.pendown()
    tess.fd(25)
    tess.penup()
    tess.fd(15)
    tess.stamp()
    tess.home()
    tess.right(turn)
    turn+=30
