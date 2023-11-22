Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 02:47:15) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 42,000
(42, 0)
>>> 4200
4200
>>> 42000
42000
>>> type(42,000)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    type(42,000)
TypeError: type() takes 1 or 3 arguments
>>> type((42,000))
<class 'tuple'>
>>> x=1
>>> y= 20
>>> y=20/2
>>> type(y)
<class 'float'>
>>> y=
SyntaxError: invalid syntax
>>> y
10.0
>>> p=5
>>> p=p+1
>>> p
6
>>> class= "welcome to CSC 110"
SyntaxError: invalid syntax
>>> x,y,z=1,2,3
>>> x=5+x
>>> y=y*4
>>> z=z-2
>>> x
6
>>> y
8
>>> z
1
>>> len("traalalallala")
13
>>> N=(4,7,10,40)
>>> mean(4,7,10,40)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    mean(4,7,10,40)
NameError: name 'mean' is not defined
>>> len(N)
4
>>> sum(N)
61
>>> N/4
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    N/4
TypeError: unsupported operand type(s) for /: 'tuple' and 'int'
>>> M=N/4
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    M=N/4
TypeError: unsupported operand type(s) for /: 'tuple' and 'int'
>>> sumAcum=0
>>> forn n in N:
	
SyntaxError: invalid syntax
>>> for n in N:
	sumAcum += n

	
>>> Avg= sumAcum/len(N)
>>> Avg
15.25
>>> 14*8
112
>>> **
SyntaxError: invalid syntax
>>> 2 ** 2
4
>>> 2 ** 3
8
>>> 
