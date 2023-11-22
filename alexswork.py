sum_accum=0
response1=input('What is your first number')
response2=input('What is your second number')
response3=input('What is your third number')
a= float(response1)
b= float(response2)
c= float(response3)
for x in [a,b,c]:
    sum_accum = sum_accum + x**3
    print(sum_accum)
