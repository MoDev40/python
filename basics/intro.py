print("Hello Python")

import sys

print(sys.version)

# Variables are value holders

"""
1: A variable name must start with a letter or the underscore character
2: A variable name cannot start with a number
3: A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
4: A variable name cannot be any of the Python keywords.
"""

x = 12
helloWorld = "Hello World!"

print(x)
print(helloWorld)

my_name = "Mdev"  # Snake Case
MyName = "Mdev"  # Pascal Case
myName = "Mdev"  # Camel Case

print(my_name)
print(MyName)
print(myName)

# Multi value assign

size, weigth = 10, 20

print(size)
print(weigth)

print(size, weigth, sep=",")

fruits = ["Banana", "Orange"]

banana, orange = fruits

print(banana)
print(orange)

globalVar = "Let it go"


def go():
    globalVar = "Go away and don't look back"  # This becomes local
    print(globalVar)


print(globalVar)
go()

print(type(banana))

# Exercise

danger = input("Is this zone is danger area? ")

print(f"Is this zone is danger area {danger}")

a, b, c = 3, 3, 10

print(a + b - c)
