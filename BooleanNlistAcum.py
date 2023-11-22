def findInts_1():
    '''returns a list of ints between 1 and 100
that are div by 2 and div by 3'''
    ##set up and empty list container
    L = [] ##list accumulator
    ## go through all ints from 1 to 100 inclusive
    ## check each int to see if it satisfies the booleans
    ## if the int satisfied the boolean, put it into L
    for n in range(1,101):
        divBy2 = (n % 2 == 0) ##true only if n is div by 2
        divBy3 = (n % 3 == 0) ##true only if n is div by 3
        Boolean = divBy2 and divBy3
        if Boolean:
            L.append(n)
    return L
##Return L

##Expecting [6,12,18,24,...]
print(findInts_1())



##Find the sum of the ints from 1 to 100 inclusive
##that are div by 2 and dive by 3

goodInts = findInts_1()
sumAcum = 0
for n in goodInts:
    sumAcum += n
print('the sum of the ints that qualify is', sumAcum)
print()
print('the sum of the ints that qualify is', sum(goodInts))


##Find the avg of the ints from 1 to 100 inclusive that are divisible by 2 and
##divisible by 3

sumAcum = 0
counter = 0
for n in goodInts:
    sumAcum += n
    counter += 1

print('the avg of the ints that qualify is', sumAcum/counter)
print()
print('The avg of the ints that qualify is', sum(goodInts)/len(goodInts))



def findInts_2():
    L = []

    for n in range(1,101):
        divBy2 = (n % 2 == 0)
        divBy3 = (n % 3 == 0)
        Boolean = divBy2 and divBy3
        if Boolean:
            L.append(n)

    return L,sum(L),sum(L)/len(L)

L,S,A = findInts_2()
print(L)
print(S)
print(A)
        
































