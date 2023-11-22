##second_turtle.py

import turtle
wn = turtle.Screen()
##BC = input('Please enter a background color: ')
wn.bgcolor("lightgreen") # Set the window background color
wn.title("Hello, Tess!") # Set the window title

tess = turtle.Turtle()

##PC = input("Please enter the t's pencolor: ")
tess.color("magenta")
##tess.color("blue") # Tell tess to change her color
##PS = input("Please enter the t's pen size: ")
##tess.pensize(7) # Tell tess to set her pen width
tess.pensize(3) # Tell tess to set her pen width
##tess.speed(0) ## fastest animated turtle

##tess.fd(50)
##tess.lt(120)
##tess.fd(50)

## have tess draw a triangle with each side having length of 50
##tess.fd(50)
##tess.lt(120)
##
##tess.fd(50)
##tess.lt(120)
##
##tess.fd(50)
##tess.lt(120)

## automates a triangle
##for i in range(3):
##    tess.fd(50)
##    tess.lt(120)


## automate a square
##for i in range(4):
##    tess.fd(100)
##    tess.lt(90)

## automate a pentagon
##turnNgl = 360/5
##for i in range(5):
##    tess.fd(100)
##    tess.lt(turnNgl)
    
## automate an octagon
##turnNgl = 360/8
##for i in range(8):
##    tess.fd(100)
##    tess.lt(turnNgl)

    
### 1st side
##tess.forward(100)
##tess.left(90)
### 2nd side
##tess.forward(100)
##tess.left(90)
### 3rd side
##tess.forward(100)
##tess.left(90)
### 4th side
##tess.forward(100)
##tess.left(90)

#### square of length 100
##for i in range(4):  ## note that loop variable i is not explicitly used inside loop
##    tess.forward(100)
##    tess.left(90)

## function for square of length 100
def square(t):
    '''Turtle t draws a square of size 100.
'''
    for i in range(4):
        t.fd(100)
        t.lt(90)

##square(tess)  ## this is the code

def square_1(t,Size):
    '''Turtle t draws a square of size Size.
'''
    for i in range(4):
        t.fd(Size)
        t.lt(90)

##square_1(tess,150)  ## this is the code


## this is the code
##for i in range(5):
##    square_1(tess,150)
##    tess.lt(360/5)

## colored square
##for c in ['red','green','blue','yellow']:
##    tess.color(c)
##    tess.fd(100)
##    tess.lt(90)

def pinWheel(t,Size,n):
    '''Turtle t draws a sqr of size Size, then turns 360/n,
and draws n sqrs, turning 360/n after each sqr.'''
    trn_ngl = 360/n
    for i in range(n):
        square_1(t,Size)
        t.lt(trn_ngl)
        
##pinWheel(tess,200,12)    
        
#### triangle of length 100
##for i in range(3):
##    tess.forward(100)
##    tess.left(120)



## pentagon of length 100
##for i in range(5):
##    tess.fd(100)
##    tess.lt(72)
    


## 8-sided regular polygon of length 100
##trn_ngl = 360/8
##for i in range(8):
##    tess.fd(100)
##    tess.lt(trn_ngl)

## function for square of length 100
## function for square of length sz
## function for regular n-sided polygon of length Size using turtle t

def polygon(t,Size,n):
    '''Turtle t draws a regular n-sided polygon of size Size.'''
    trn_ngl = 360/n
    for i in range(n):
        t.fd(Size)
        t.lt(trn_ngl)


## what does this do?
## reposition t lower on the turtle screen
tess.pu()
tess.lt(90)
tess.bk(100)
tess.rt(90)
tess.pd()
tess.speed(0)
for n in range(3,13):
    polygon(tess,150,n)
    

## tess draws a dodecagon with sizes 100 long
##polygon(tess,50,12)

## move tess 200 down
##tess.pu()
##tess.rt(90)
##tess.fd(200)
##tess.lt(90)
##tess.pd()

## draw the dodecagon
##polygon(tess,100,12)

def pinWheel_1(t,Size,n,m):
    '''Turtle t draws a regular n-sided polygon of size Size, then turns 360/n,
and draws m polygons, turning 360/m after each polygon.'''
    trn_ngl = 360/m
    for i in range(m):  ## loop for drawing the m polygons
        polygon(t,Size,n)
        t.lt(trn_ngl)

##for n in range(4,9,2):
##    pinWheel_1(tess,100,n,5)
    

##pinWheel_1(tess,150,8,4)
        
    
##for i in range(5):
##    tess.fd(100)
##    tess.lt(72)


##def polygon(t,size,n_sides):
##    '''Turtle t draws a regular polygon with side length,
##size, and num of sides of n_sides.'''
##    for i in range(n_sides):
##        t.fd(size)
##        tess.lt(360/n_sides)
##
####polygon(tess,100,8)
##
####for n_sides in range(3,13):
####    polygon(tess,100,n_sides)
##def square():
##    '''Use tess to draw a square 100 on a side.'''
##    for i in range(4):
##        tess.fd(100)
##        tess.lt(90)
##        
##
##def square(t,size):
##    '''Turtle t draws a square of side length size.'''
##    for i in range(4):
##        t.fd(size)
##        t.lt(90)
##
##def square_1(t,ps,pc,size):
##    '''Turtle t draws a square of side length size using pensize ps
##and pencolor pc.'''
##    tess.color(pc)
##    tess.pensize(ps)
##    for i in range(4):
##        t.fd(size)
##        t.lt(90)
##
##def pinwheel(t,size):
##    '''Draw 12 squares, rotation 30 deg between each square.'''
##    for i in range(12):
##        square(t,size)
##        t.lt(30)
##
##def pinwheel_1(t,size):
##    '''Draw 12 squares, rotation 30 deg between each square.'''
##    for i in range(12):
##        for i in range(4):
##            t.fd(size)
##            t.lt(90)
##
##def pinwheel_2(t,ps,pc,size):
##    '''Draw 12 squares, rotation 30 deg between each square.'''
##    for i in range(12):
##        square_1(t,ps,pc,size)
##        t.lt(30)      
##
####pinwheel(tess,100)
##
####pinwheel_1(tess,100)
##
####square(200, tess)
####square_1(tess,200)
##
####pinwheel_2(tess,7,'yellow',200)
##
####t,ps,pc,size =  tess,7,'yellow',200      
####pinwheel_2(t,ps,pc,size)
##
##square()    
##    
