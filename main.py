x = lambda a, b: a + b

print(x(2, 4))


def my_fn(n):
    return lambda a: a**n


multiplier = my_fn(7)
print(multiplier(2))

import array

x = array.array("i", [1, 2, 3, 4, 5])
cars = ["Ford", "Volvo", "BMW"]
print(type(x))
print(x)
print(type(cars))
print(cars)


def myfunc():
    x = "Hello"
    print(x)

    def myfunc2():
        nonlocal x
        x = "Hi"
        print(x)

    myfunc2()
    return x


print(myfunc())

from basics import mymodule

mymodule.say_hi()
mymodule.say_thanks()
print(mymodule.user)
print(mymodule.get_platform())
print(dir(mymodule))

from basics.mymodule import user

print(user)


try:
    print(xz)
except NameError as ne:
    print(ne)
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("Finally finished")

try:
    f = open("demo.txt", "r")
    try:
        f.write("Hello")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")

deci = "k"

try:
    if not type(deci) is int:
        raise TypeError("Decision must be an integer")
except Exception as e:
    print(e)

price = 59
print(f"The price is ${price:.2f} dollars")

fruit = "Apple"

print(f"We love {fruit.upper()}")
