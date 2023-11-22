def SumOfSqrOfInts_A(From,To):
    for n in range(From,To+1):
        a7= (n%7==0)
        a3= (n%3==0)
        a2= (n%2==0)
        B= a2 and (a7 or a3)
        if B:
            

SumOfSqrOfInts_A(20,40)


def SumOfSqrOfInts_B(From,To):
    for n in range(From,To+1):
        a7= (n%7==0)
        a3= (n%3==0)
        a2= (n%2==0)
        B= (a3 and a7) or a2
        if B:
            print(n**2)

##SumOfSqrOfInts_B(20,40)
