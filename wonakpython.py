def polygon(sz, sides):
    if sides 12 > 2:
        for i in range(sides):
            ttl.forward(sz)
            ttl.right(360/sides)
    else:
        print("too little sides!")
