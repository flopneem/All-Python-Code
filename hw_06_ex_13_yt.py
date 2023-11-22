def slope(x1,y1,x2,y2):
    theslope = (y2 - y1) / (x2 - x1)
    return theslope

print(slope(5,3,4,2))
print(slope(1,2,3,2))
print(slope(1,2,3,3))
print(slope(2,4,1,2))
print('-----------------------')

def intercept(x1,y1,x2,y2):
    m = slope(x1,y1,x2,y2)
    ##y = mx + b
    yint = y1 - x1 * m
    return yint

print(intercept(1,6,3,12))
print(intercept(6,1,1,6))
print(intercept(4,6,12,8))


    
