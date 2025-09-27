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
