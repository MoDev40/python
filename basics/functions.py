def say_hello(name: str):
    print("Hello {}".format(name))


say_hello("Mdev")


def calculate_sum(a: float, b: float) -> float:
    """
    :param a: is a float number and must be greater than 0
    :param b: is a float number and must be greater than 0
    :return: sum of a, b the value type is a float
    """
    if a <= 0 or b <= 0:
        raise ValueError("a and b must be greater than 0")
    return a + b


try:
    print(calculate_sum(1, -2))
except ValueError as e:
    print(e)


def say_hi():
    print("Hi everyone!")


say_hi()


def say_hello(f_name):
    print(f"Hello, {f_name}")


say_hello("John")
say_hello("Alia")


def student(name, age):
    print(f"Hello, {name}, you are {age} years old.")


student("John", 25)


def print_hobbies(*hobbies):
    print(hobbies)


print_hobbies(1, 2, 3, 4)


def show_attends(*args):
    print(f"Total attends: {len(args)}")
    for attend in args:
        print(f"Hello {attend} welcome we are happy to see you.")


show_attends("John", "Alia", "Jane", "Hani", "Omar")

student(age=33, name="Aisha")


def team_announcement(**kwargs):
    print(kwargs)


team_announcement(alia="Alia", hassan="Hassan", hani="Hani")


def is_active(active=True):
    print("Active" if active else "Inactive")


is_active(False)
is_active()


def max_value(data: list) -> float:
    return max(data)


print(max_value([1, 2, 3]))


def positional_arg_only(a, b, /):
    print(a + b)


positional_arg_only(3, 6)
positional_arg_only(3, 6)


def keyword_arg_only(*, a, b):
    print(a + b)


keyword_arg_only(a=6, b=8)
keyword_arg_only(a=7, b=4)
