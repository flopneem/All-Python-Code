import turtle
wn = turtle.screen()
sz = 100

def plus(t,sz):
    '''turtle will draw a plus'''
    for i in range(4):
        t.foward(sz)
        t.left(180)
        t.foward(sz*2)
        t.left(180)
        t.foward(sz)
        t.left(90)
        t.foward(sz)
        t.right(180)
        f.foward(sz*2)

    wn.mainloop()

def rowofpluses(tess, 25,4,70):
    for i in range(n):
        plus(t,sz)
        t.pu()
        t.fd()
        t.fd(1.5*sz)
        t.pd()
