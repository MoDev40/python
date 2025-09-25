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


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def get_email(self):
        return self.email


class Student(User):
    def __init__(self, first_name: str, last_name: str, email: str, password: str):
        User.__init__(self, email=email, password=password)
        self.first_name = first_name.title()
        self.last_name = last_name.title()

    def print_full_name(self):
        print(self.first_name, self.last_name)


student = Student(
    first_name="jane", last_name="doe", email="janedoe@gmail.com", password="12345"
)
student.print_full_name()
print(student.get_email())


class Teacher(User):
    def __init__(self, first_name: str, last_name: str, email, password, age):
        super().__init__(email, password)
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age

    def print_full_name(self):
        print(self.first_name, self.last_name)

    def get_email(self):
        print(self.email)

teacher = Teacher('Hassan','Salah','salahhassan@gmail.com','1299613',33)
teacher.print_full_name()
teacher.get_email()
