## Karen Ma
## Professor Wellman
## CSC 110 - Extra Credit 6
## 17 Nov 2019

## YOUTUBE LINK: https://youtu.be/wFSqXLoPseM
## Write a python code to make a x and y azis and a background grid.
## Spec: Axes 600 long each and center at (0,0)
##       Axes are black and made with penwidth of 5
##       Background grid has spacing of 25 and is light blue with penwith 3
##       After drawing axes draw the function:
##       f(x) = (1/6)x^2 - (1/12)x - 7.5 from - 10 <= x <= 10 in steps of 1/4
##       Put green crosses at all the intergers
##       Use helper functions.

import turtle

def makeScreen(bgcolor,title):
    '''Returns a window for the turtle to draw on'''
    wn = turtle.Screen()
    wn.bgcolor(bgcolor)
    wn.title(title)
    return wn

def makeTurtle(color,size,speed):
    '''Returns turtles that draws images into the window'''
    t = turtle.Turtle()
    t.pensize(size)
    t.color(color)
    t.speed(speed)
    return t

def makeCross(t,amount):
    '''Make a cross. I used this to make the Axis and green markers on the
graph'''
    t.pd()
    for i in range(4):
        t.fd(amount//2)
        t.bk(amount//2)
        t.rt(90)
        
def linesGrid(t,spacing,amount):
    '''Makes the lines for the grid'''
    for i in range(2): 
        t.pd()
        for i in range(12): ## Loops to draw the lines
            t.fd(amount)
            t.pu()
            t.bk(amount)
            t.rt(90)
            t.fd(spacing)
            t.lt(90)
            t.pd()
        t.pu()
        t.rt(90)
        t.fd(spacing)
        t.lt(90)
    t.lt(90)
    t.fd(amount + spacing*2)
    t.rt(90)

def makeGrid(t,spacing,amount):
    '''Makes the horizontal and vertical line of the grid'''
    t.pu()
    t.bk(amount//2)
    t.lt(90)
    t.fd(amount//2)
    t.rt(90)
    linesGrid(t,spacing,amount) ## Makes the horizontal lines
    t.fd(amount)
    t.rt(90)
    linesGrid(t,spacing,amount) ## Makes the vertical lines
    t.ht()

def makeFunction(t,s):
    '''Creates the function of the graph and plots it onto the grid'''
    t.pu()
    for i in range(-10,10+1):
        y = ((1/6)*((i)**2) - ((1/12)*i) - 7.5) ## Draws the given function on the grid
        t.goto(i*s,y*s) ## Moves the turtle directly to a coordinate on the grid
        t.pd()
        t.color("green") 
        makeCross(t,s//2) ## Makes the cross mark for each int point
        t.color("red")
    t.ht()

wn = makeScreen("White","Extra Credit 06 - Plot the Function")
turtleAxis = makeTurtle("black",3,0)
turtleGrid = makeTurtle("Lightblue",1,0)
turtleGCross = makeTurtle("red",2,0)

makeCross(turtleAxis,600)
turtleAxis.ht()
makeGrid(turtleGrid,25,600)
makeFunction(turtleGCross,25)
