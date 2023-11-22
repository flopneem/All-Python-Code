import turtle
wn = turtle.screen()
wn.bgcolor('lightblue')
tess = turtle.Turtle()
tess.color('green')

#Q1
def squareFromCenter(t,sz):
    '''Turtle draws a square'''
    for i in range(4):
        t.pu()
        t.fd(sz/2)
        t.lt(90)
        t.fd(sz/2)
        t.pd()
        t.lt(sz)

#squareFromCenter(tess,50)

#Q2
def squareFromCenterRotCCW(t,sz,ngl):
    '''Drawing a rotated circle from the center'''
    for i in range(4):
        t.lt(ngl)
        squareFromCenter(t,sz)

#squareFromCenterRotCCW(tess,50,45)

#Q3
def rowOfRotatedSqrs(t,sz,ngl,spc,n):
    '''row of rotated squares'''
    for i in range(n):
        squareFromCenterRotCCW(t,sz,ngl)
        t.pu()
        t.fd(spc)
        t.pd()

#rowOfRotatedSqrs(tess,50,45,60,5)

def rowOfRotatedSqrs(t,sz,ngl,spc,n):
    '''row of rotated squares'''
    for i in range(n):
        squareFromCenterRotCCW(t,sz,ngl)
        t.pu()
        t.fd(spc)
        t.pd()

#rowOfRotatedSqrs(tess,50,30,60,5)


#Q4
def sqrOfRotatedSqrs(t,sz,ngl,spc,n):
    '''row of a row of rotated squares'''
    for i in range(4):
        rowOfRotatedSqrs(t,sz,ngl,spc,n)
        t.pu()
        t.fd(spc)
        t.pd()
        t.lt(90)

#sqrsOfRotatedSqrs(tess,50,45,60,5)


def sqrsOfRotatedSqrs(t,sz,ngl,spc,n):
    '''row of a row of rotated squares'''
    for i in range(4):
        rowOfRotatedSqrs(t,sz,ngl,spc,n)
        t.pu()
        t.fd(spc)
        t.pd()
        t.lt(90)

#sqrsOfRotatedSqrs(tess,50,30,60,5)
