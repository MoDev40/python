# 1

"""
first take input from the user
second create a function that takes two arguments a:float,b:float
third validate,calculate and print out
"""

input_a = float(input("Enter first number: "))
input_b = float(input("Enter second number: "))


def calculator(a: float, b: float):
    print(f"The sum of {a} and {b} is {a+b}")
    print(f"The difference of {a} and {b} is {a-b}")
    print(f"The product of {a} and {b} is {a*b}")
    print(f"The quotient of {a} and {b} is {a//b}")
    print(f"The reminder of {a} and {b} is {a%b}")


calculator(input_a, input_b)

# 2
"""
	first create variables a=5 b=10
	second prepare swiping methods hint use arithmetic operations
"""

a = 5
b = 10

print(f"a = {a}")
print(f"b = {b}")

b -= a
print(f"b = {b}")
a += a
print(f"a = {a}")

# 3
"""
	first create variables item,price,quantity
	second print out using only string concatenation and type conversion
"""
item = "Pens"
price = 2.5
quantity = 4

print(
    "You bought "
    + str(quantity)
    + " "
    + item
    + " for total of "
    + str(quantity * price)
    + " dollars."
)
