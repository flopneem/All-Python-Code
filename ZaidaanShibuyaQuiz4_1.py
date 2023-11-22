def findInts():
    L = []
    for n in range(1,501):
        divBy60 = (n % 60 == 0)
        divBy90 = (n % 90 == 0)
        Boolean = divBy60 and divBy90
        if Boolean:
            L.append(n)
    return L
findInts()

print(findInts())

Listaccum = findInts()

print(sum(Listaccum)/len(Listaccum))

