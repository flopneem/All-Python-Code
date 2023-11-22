counter = 0
sumAcum = 0

for n in range(2,251):
    divBy7 = % 7 == 0
    divBy3 = % 3 == 0
    divBy5 = % 5 == 0
    Boolean = (divBy) and (not(divBy3 or divBy))
    if Boolean:
        sumAcum += n
        counter += 1
print('The avg of ints that qualify from 2 to 250 is',round(sumAcum/counter))


