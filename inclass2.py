def addIntsl_5():
    ';;Print1 + 2 + 3 + 4 + 5'''

    sumAcum = 0
    for n in range(1,5+1):
        sumAcum = sumAcum + n
    print(sumAcum)

addIntsl_5()


def addIntsl_n(n):
    ';;Print1 + 2 + 3 + 4 + 5'''

    sumAcum = 0
    for n in range(1,n+1):
        sumAcum = sumAcum + n
    print(sumAcum)

for n in range(1,5):
    addIntsl_n(n)
