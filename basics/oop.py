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


class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        return "Move"


class Car(Vehicle):
    def move(self):
        return "Drive"


class Boat(Vehicle):
    def move(self):
        return "Sail"


class Plane(Vehicle):
    def move(self):
        return "Fly"


car = Car("Toyota")
boat = Boat("H6s12")
plane = Plane("Air32SJ11")

for x in (car, boat, plane):
    print(x.name)
    print(x.move())


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


teacher = Teacher("Hassan", "Salah", "salahhassan@gmail.com", "1299613", 33)
teacher.print_full_name()
teacher.get_email()


class Product:
    def __init__(self, name, price, quantity, is_available):
        self._name = name
        self._price = price
        self._quantity = quantity
        self.__is_available = is_available

    def set_is_available(self, is_available):
        self.__is_available = is_available

    def get_is_available(self):
        return self.__is_available


product = Product("Apple", 2, 6, True)
product._name = "Mango"
print(product.get_is_available())
product.set_is_available(False)
print(product.get_is_available())
print(product._name)

from abc import ABC, abstractmethod


class Order(ABC):
    def __init__(self, order_id, price, quantity, order_date, destination, status):
        self.order_id = order_id
        self.price = price
        self.quantity = quantity
        self.order_date = order_date
        self.destination = destination
        self.status = status

    @abstractmethod
    def pay_order(self):
        pass

    @abstractmethod
    def process_order(self):
        pass

    @abstractmethod
    def cancel_order(self):
        pass

    @abstractmethod
    def progress_order(self):
        pass


class PizzaOrder(Order):
    def __init__(
        self,
        order_id,
        price,
        quantity,
        order_date,
        destination,
        status,
    ):
        super().__init__(order_id, price, quantity, order_date, destination, status)

    def pay_order(self):
        return self.quantity * self.price

    def process_order(self):
        self.status = "Processing"
        return self.status

    def cancel_order(self):
        self.status = "Cancelled"

    def progress_order(self):
        self.status = "Delivered"
        return self.status


pizza_order = PizzaOrder("10K18NJ8", 7, 3, "6-5-2025", "K4 Mogadishu", "Created")

print(pizza_order.process_order())
print(pizza_order.pay_order())
print(pizza_order.order_id)
print(pizza_order.progress_order())


class ClothesOrder(Order):
    def __init__(
        self,
        name,
        order_id,
        price,
        quantity,
        order_date,
        destination,
        status,
    ):
        Order.__init__(self, order_id, price, quantity, order_date, destination, status)
        self.name = name

    def pay_order(self):
        return self.quantity * self.price

    def process_order(self):
        self.status = "Processing"
        return self.status

    def cancel_order(self):
        self.status = "Cancelled"
        return self.status

    def progress_order(self):
        self.status = "Delivered"
        return self.status

    def print_order_name(self):
        print(self.name)


clothes_order = ClothesOrder(
    "Barca Shirt",
    "G1985LM4R",
    9,
    1,
    "17-8-2024",
    "Waberi Mogadishu",
    "Created",
)

clothes_order.print_order_name()
print(clothes_order.order_date)
print(clothes_order.cancel_order())
