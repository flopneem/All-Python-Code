Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> (3+2)**2+1
26
>>> x = x/2
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    x = x/2
NameError: name 'x' is not defined
>>> x/2
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x/2
NameError: name 'x' is not defined
>>> x = (3+2)**2+1
>>> x = x/2
>>> print(x)
13.0
>>> a = 2
>>> b = 3
>>> x = 4*(b-a)
>>> print(x)
4
>>> a = a + 1
>>> print(a)
3
>>> b = b - 1
>>> print(b)
2
>>> 8911 // 24
371
>>> 8911 // 60
148
>>> 149 // 24
6
>>> 148 // 24
6
>>> n = 10837645697820775994467843245679991239087567806632
>>> len(n)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    len(n)
TypeError: object of type 'int' has no len()
>>> len(str(n))
50
>>> n = len('two')
>>> print(n)
3
>>> strg = 'peanut butter' + '&' + 'jelly'
>>> print(strg)
peanut butter&jelly
>>> strg*n
'peanut butter&jellypeanut butter&jellypeanut butter&jelly'
>>> User = 'Muktar'
>>> r = 6
>>> print(User ' circumference is ' r*2)
SyntaxError: invalid syntax
>>> print(User 'circumference is' r*2)
SyntaxError: invalid syntax
>>> print(User r*2)
SyntaxError: invalid syntax
>>> print(r)
6
>>> import math
>>> print(User, r*2)
Muktar 12
>>> 123 // 7
17
>>> 123 % 7
4
>>> print('returned 17 weeks and 4 days later')
returned 17 weeks and 4 days later
>>> for num in range(1,10):
	print(nu)

	
Traceback (most recent call last):
  File "<pyshell#39>", line 2, in <module>
    print(nu)
NameError: name 'nu' is not defined
>>> for num in range(1,10):
	print(num)

	
1
2
3
4
5
6
7
8
9
>>> total_inches = 555
>>> print('total inches =', total_inches)
total inches = 555
>>> begin = total_inches
>>> yards = total inches // 36
SyntaxError: invalid syntax
>>> yards = total_inches // 35
>>> yards = total_inches // 36
>>> print(yards)
15
>>> total_inches %= 36
>>> feet = total_inches // 12
>>> inches = total_inches % 12
>>> print(begin,'inches =',yards,'yards,',feet,'feet,',inches,'inches.')
555 inches = 15 yards, 1 feet, 3 inches.
>>> print('Check:', yards*36 + feet*12 + inches,'inches.')
Check: 555 inches.
>>> 
