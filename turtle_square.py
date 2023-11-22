import turtle

wn = turtle.Screen()
tess = turtle.Turtle()

def rectangle(t,W,H):
    '''Turtle t draws a rectange
of width W & height H.'''
    for i in range(2):
        t.fd(W)
        t.lt(90)
        t.fd(H)
        t.lt(90)
##still have no idea what is happening
##rectangle(tess,200,50)


##We can use the def of a rectangle
##to write the def for a square

def square(t,sz):
    '''Turtle t draws a square of size sz
using the rectange definition.'''
    rectangle(t,sz,sz)

##square(tess,200)

def pinwheel_1(t,w,h,n):
    '''uses rectangle(t,w,h,) to make a pinwheel
using turtle, t. n is an int that tells how
many rectangles to make within a turn of
360 degrees.'''
    trnNgl = 360/n
    for i in range(n):
        rectangle(t,W,H)
        t.lt(trnNgl)

pinwheel_1(tess,200,75,12)
