def addInts():
    '''a function which adds and prints out the integers'''
    S = 0
    for i in range(5,32,3):
        S += i
    print(S)

##addInts()

## want to 3,6,9,12,... n of these ints
## addMult3(n)

def addMult3(n):
    '''add 3,6,9,12,...   n of these ints,
print out the sum.'''
    S = 0
    for i in range(3,n+3,3):
        S += i
    print(S)

addMult3(2)
