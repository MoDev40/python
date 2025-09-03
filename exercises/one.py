# 1

"""
	first take input from the user
	second create a function that takes two arguments a:float,b:float
	third validate,calculate and print out
"""

input_a = float(input('Enter first number: '))
input_b = float(input('Enter second number: '))

def calculator(a:float,b:float):
	print(f'The sum of {a} and {b} is {a+b}')
	print(f'The difference of {a} and {b} is {a-b}')
	print(f'The product of {a} and {b} is {a*b}')
	print(f'The quotient of {a} and {b} is {a//b}')
	print(f'The reminder of {a} and {b} is {a%b}')


calculator(input_a,input_b)