Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 02:47:15) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 1,000,000
(1, 0, 0)
>>> zipcode = 02492
SyntaxError: invalid token
>>> minute = 59
>>> minute?/60.0
SyntaxError: invalid syntax
>>> minute/60.0
0.9833333333333333
>>> miles = 26.2
>>> miles * 1.61
42.182
>>> x=5
>>> x+1
6
>>> first = 'throat'
>>> second = 'wobbler'
>>> first+second
'throatwobbler'
>>> 'spam'*3
'spamspamspam'
>>> width = 17
>>> height = 12.0
>>> delimiter = '.'
>>> width*2
34
>>> width*2.0
34.0
>>> height*3
36.0
>>> 1+2+*5
SyntaxError: invalid syntax
>>> 1+2*5
11
>>> 4*3
12
>>> 4/3
1.3333333333333333
>>> ((4/3)*(3.14)*(5))^3
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    ((4/3)*(3.14)*(5))^3
TypeError: unsupported operand type(s) for ^: 'float' and 'int'
>>> 5^3
6
>>> 5*5*5
125
>>> (4/3)*(3.14)*(5^3)
25.119999999999997
>>> 24.95*.4
9.98
>>> 24.95*60
1497.0
>>> 9.98*60
598.8000000000001
>>> 1497-598.8
898.2
>>> .75*59
44.25
>>> type(32)
<class 'int'>
>>> import math
>>> print math
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(math)?
>>> print (math)
<module 'math' (built-in)>
>>> ratio = signal_power / noise power
SyntaxError: invalid syntax
>>> ratio - signal_power / noise_power
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    ratio - signal_power / noise_power
NameError: name 'ratio' is not defined
>>> ratio=signal_power / noise_power
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    ratio=signal_power / noise_power
NameError: name 'signal_power' is not defined
>>> import math
>>> ratio = signal_power / noise_power
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    ratio = signal_power / noise_power
NameError: name 'signal_power' is not defined
>>> def print_lyrics():
	print "Im a lumberjack, and im okay"
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Im a lumberjack, and im okay")?
>>> import math
>>> print math
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(math)?
>>> print (math)
<module 'math' (built-in)>
>>> decibels = 10*math.log10(ratio)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    decibels = 10*math.log10(ratio)
NameError: name 'ratio' is not defined
>>> def print_lyrics():
	print "I'm a lumberjack and im okay"
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("I'm a lumberjack and im okay")?
>>> 
KeyboardInterrupt
>>> def print_lyrics():
	print "im a lumberjack and im okay"
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("im a lumberjack and im okay")?
>>> def print_lyrics()
"im a lumberjack and im okay. i sleep all night and i work all day"
def repeat_lyrics():
  print_lyrics()
  print_lyrics()
repeat_lyrics()
  
