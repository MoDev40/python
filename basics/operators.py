# Arithmetic operator
"""
	+ addition
	- subtraction
	/ division
	% modulus
	* multiplication
	** exponentiation
	// floor division
"""

print("## Arithmetic operators ##")
print(10+10)
print(22-19)
print(8/3)
print(5*10)
print(3**2)
print(8//3)
print(8%2)

# Assignment operators
"""
 =
 +=
 -=
 *=
 and much more
"""

print("## Assignment operators ##")
x = 6
x+=3 # same as x = x+3
print(x)
x//=4 # same as x = x//4
print(x)
x*=3
print(x)
x**=3
print(x)
x/=4
print(x)
x%=2
print(x)

# Comparison operator
"""
	== equal
	!= not equal
	> grater than
	>= greater than equal
	< less than
	<= less than equal
"""

print("## Comparison operators ##")

print(5==5)
print(5==3)
print(8>4)
print(4>8)
print(8>=8)
print(16<9)
print(9<10)
print(10<=10)
print(3!=6)
print(6!=6)

# Logical Operator
"""
	and
	or
	not
"""

print("## Logical operators ##")

age = 51
w = 70
if age >= 50 and w > 70:
	print('Yes')

if age > 50 or w > 70:
	print('May be')

if not age < 50:
	print('Age not less than 50')
	
# Identity operators

w=5
l = 'Hi'

if w is not l:
	print('W is not l')
	
b = 'Hi'
if l is b:
	print('L is b')
	
# Membership operator

a = ['banana','apple','mango']
search = 'onion'

if search in a:
	print('Yes we have')
	
if search not in a:
	print('We don\'t have this item please search else where')