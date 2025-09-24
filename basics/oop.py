class Myclass:
    x = 5


x1 = Myclass()

print(x1.x)


class Person:
    def __init__(self, name, age, is_active):
        self.name = name
        self.age = age
        self.is_active = is_active

    def __str__(self):
        return f"name:{self.name} age:{self.age}"

    def get_name(self):
        return self.name


person = Person("Jane Doe", 33, True)
print(person.name)
print(person.age)
print(person.is_active)
person.age = 45
del person.is_active
print(person)
print(person.get_name())


class Car:
    pass


car = Car()
del car
