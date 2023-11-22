##https://youtu.be/D_LhWG1al4k

import turtle 
tess = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("Lightgreen")
tess.pensize(5)


def mltyClrdSqr(t ,sz,clr1, clr2, clr3, clr4):
    for x in (clr1, clr2, clr3, clr4):
        tess.color(x)
        tess.fd(sz)
        tess.left(90)

mltyClrdSqr(tess,150,'red', 'green', 'blue', 'magenta')


def lineOfMltyClrdSqrs(t, sz, clr1, clr2, clr3, clr4, spc, n):
    for x in range(5):
        mltyClrdSqr(t ,sz,clr1, clr2, clr3, clr4)
        tess.pu()
        tess.fd(sz+spc)
        tess.pendown()
##lineOfMltyClrdSqrs(tess,50,'red','green','blue','magenta',20,6)


def sqrOfLineOfMltyClrdSqrs(t, sz, clr1, clr2, clr3, clr4, spc, n):
    for x in range (4):
        lineOfMltyClrdSqrs(t, sz, clr1, clr2, clr3, clr4, spc, n)
        tess.left(90)
        tess.pu()
        tess.fd(sz)
        tess.pendown()
##sqrOfLineOfMltyClrdSqrs(tess,35,'red','green','blue','magenta',25,5)
