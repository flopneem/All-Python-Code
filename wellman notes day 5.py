 def addsConsecInts(n1,n2):
	'''Add ints
	n1, n1+1, n1+2,...,n2.'''
	sumAcum = 0
	for n in range(n1,n2+1):
            sumAcum += n
        print(sumAcum)

addsConsecInts(1,4)
