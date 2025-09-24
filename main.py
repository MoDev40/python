x = lambda a,b : a+b

print(x(2,4))

def my_fn(n):
	return lambda a : a**n

multiplier = my_fn(7)
print(multiplier(2))

import array

x = array.array('i',[1,2,3,4,5])
cars = ["Ford", "Volvo", "BMW"]
print(type(x))
print(x)
print(type(cars))
print(cars)
