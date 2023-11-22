import turtle
from time import sleep 
turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor('lightgreen')
tess = turtle.Turtle()
alex = turtle.Turtle()
megatron = turtle.Turtle()
def draw_housing():
    tess.pensize(3)
    tess.color("black","darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40,180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()

tess.penup()
tess.forward(40)
tess.left(90)
tess.forward(50)
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

alex.penup()
alex.forward(40)
alex.left(90)
alex.forward(120)
alex.shape("circle")
alex.shapesize(3)
alex.fillcolor("darkorange")

megatron.penup()
megatron.forward(40)
megatron.left(90)
megatron.forward(190)
megatron.shape("circle")
megatron.shapesize(3)
megatron.fillcolor("darkred")

state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0:
        tess.fillcolor("green")
        alex.fillcolor("orange")
        state_num = 1
    elif state_num == 1:
        tess.fillcolor("darkgreen")
        alex.fillcolor("orange")
        state_num = 2
    elif state_num == 2:
        alex.fillcolor("darkorange")
        megatron.fillcolor("red")
        state_num = 3
    else:
        megatron.fillcolor("darkred")
        tess.fillcolor("green")
        state_num = 0

while(True):
    sleep(3)
    advance_state_machine()
    sleep(1)
    advance_state_machine()
    sleep(1)
    advance_state_machine()
    sleep(2)
    advance_state_machine()
    

    
wn.listen()
wn.mainloop()
