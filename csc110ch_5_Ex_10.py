def find_hypotenuse(A, B):
    return ((A**2 + B**2) ** 0.5)

A=int(input("What is your first side length?"))

B=int(input("What is your second side length?"))

print("the hypotenuse of a 90degree triangle with sides", A, "and",B, "is",find_hypotenuse(A,B))
