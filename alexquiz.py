##QUESTION 1
print("Question 1")
print("----------")
def LtrValue(Ltr):
    
    if('A' <=Ltr<= 'G'):
        return 10
    elif('H'<=Ltr<='N'):
        return 20
    elif('O'<=Ltr<='U'):
        return 30
    elif('V'<=Ltr<='Z'):
        return 40
    else:
        return(0)
for Ltr in 'ADG iHL-N':
    print(Ltr,'has value',LtrValue(Ltr))
print()
##QUESTION 2
print("Question 2")
print("----------")
Word= str('ABE')
def WordValue(Word):
    s=0
    for x in Word:
        s=s+LtrValue(x)
    return(s)
print(Word,'has value',WordValue(Word))

Word= str('OPRA')
def WordValue(Word):
    s=0
    for x in Word:
        s=s+LtrValue(x)
    return(s)
print(Word,'has value',WordValue(Word))

Word= str('OPRA-JONES')
def WordValue(Word):
    s=0
    for x in Word:
        s=s+LtrValue(x)
    return(s)
print(Word,'has value',WordValue(Word))
print()
##QUESTION 3
print("Question 3")
print("----------")
def ListOfWordSumProd(LOfWord):
   sumWord=0
   prodWord=1
   for Word in LOfWord:
       sumWord+=WordValue(Word)
       prodWord*=WordValue(Word)
   return [sumWord,prodWord]
ListOfWordSumProd=ListOfWordSumProd(["ABE",'OPRA','OPRA-JONES'])
print("The sum of the values of the words is",ListOfWordSumProd[0])
print("The product of the values of the words is",ListOfWordSumProd[1])
print()
##Question 4
print("Question 4")
print("----------")
def ListOfWordSumProd(LOfWord):
   sumWords=0
   prodWords=1
   for Word in LOfWord:
       sumWords+=WordValue(Word)
       prodWords*=WordValue(Word)
   return [sumWords,prodWords]

def ProductBySum(Name):
   L=ListOfWordSumProd(Name)
   res=L[1]/L[0]
   return round(res,2)

L=ListOfWordSumProd(['ZAIDAAN-SHIBUYA'])
print('The sum of the values of the words is',L[0])
print('The product of the values of the words is',330*ProductBySum('ZAIDAANSHIBUYA'))

zaidaan=(330*ProductBySum('ZAIDAANSHIBUYA'))/L[0]
print("Product of valuess divided by Sum of values", zaidaan)
