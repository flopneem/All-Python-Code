def is_rightangle(x,y,z):
    sides_list = [x,y,z]

    sides_list.sort()

    length1 = sides_list[0]

    length2 = sides_list[1]

    hypotenuse = sides_list[2]

    legs_squared = length1**2 + length2**2

    hypotenuse_squared = hypotenuse**2

    ratio = hypotenuse_squared / legs_squared

    ratio_error = abs(1 - ratio)

    if ratio_error < (1*10**-10):
        print('true')

    if ratio_error >(1*10**-10):
        print("False")

x=int(input("What is your first side length?"))

y=int(input("What is your second side length?"))

z=int(input("What is your thirs side length?"))

print(is_rightangle(x,y,z))
