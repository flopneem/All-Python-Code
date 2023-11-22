import turtle
wn = turtle.Screen()
wn.bgcolor('lightgreen')
tess = turtle.Turtle()


def dashedLine(Ln,nDashes):
    '''Turtle t draws a dashed line of length Ln,
using nDashes'''
    dashLength = Ln/nDashes + nDashes - 1
    for i in range(nDashes - 1):
        t.fd(dashLength)
        t.pu()
        t.fd(dashLength) 
        t.pd()
    t.fd(dashLength)

    
    
tess.ht()
dashedLine(tess,100,7)
