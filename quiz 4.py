def SumOfSqrOfInts_A(From,To):
    for n in range(From,To+1):
        a7= (n%7==0)
        a3= (n%3==0)
        a2= (n%2==0)
        B= a2 and (a7 or a3)
        if B:
            print(n**2)
    QI=[24,28,30,36]
    CS=0
    for a in QI:
        CS+=a**2
    S= 24**2 +28**2 +30**2 + 36**2
    print("Qualifying ints are ",QI)
    print("Checked sum is ",CS)
    print("Sum_A is",S)
    print("function return is", S)

##SumOfSqrOfInts_A(20,40)

def SumOfSqrOfInts_B(From,To):
    for n in range(From,To+1):
        a7= (n%7==0)
        a3= (n%3==0)
        a2= (n%2==0)
        B= (a3 and a7) or a2
        if B:
            print(n**2)
    QI=[20,21,22,24,26,28,30,32,34,36,38,40]
    CS=0
    for a in QI:
        CS+=a**2
    S= 20**2+21**2+22**2+24**2+26**2+28**2+30**2+32**2+34**2+36**2+38**2+40**2
    print("Qualifying ints are ",QI)
    print("Checked sum is ",CS)
    print("Sum_B is",S)
    print("function return is", S)

SumOfSqrOfInts_B(20,40)






