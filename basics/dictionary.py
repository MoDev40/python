car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(car)
print(type(car))
print(car.keys())
print(car.values())
print(car["year"])
print(car["model"])
print(len(car))

student = {
    "name": "Osama",
    "age": 23,
    "courses": ["Python", "JS", "React"],
    "is_active": True,
}

keys = student.keys()
values = student.values()

print(student)
print(student.get("courses"))
print(student["is_active"])
print("before update", [keys, values])
student["location"] = "KM4"
student["is_active"] = False
print("after update", [keys, values])
print("Items ", student.items())
if "is_active" in student:
    print("is_active key is in student")

print(dict(color="Red", type="Electric", price=20, period="2m"))

print(car)
car["year"] = 2003
print(car)
car.update({"model": "Electric"})
print(car)
car["color"] = "black"
print(car)
car.pop("color")
print(car)
del car["model"]
print(car)
car.popitem()
print(car)
car.clear()
print(car)
# Looping
for x in student:
    print(x)  # keys

for x in student:
    print(student[x])  # values

for x in student.values():
    print(x)

for key, value in student.items():
    print(key, value, sep=" : ")

car2 = car.copy()
student2 = dict(student)
student["name"] = "alia"
print(car2)
print(student2)
print(student)

# Nested
users = {
    "1": {
        "name": "Alia",
        "password": "12345678",
        "email": "alia@gmail.com",
    },
    "2": {
        "name": "Ahmed Ali",
        "password": "aliahmed@12",
        "email": "amhedali201@gmail.com",
    },
}

print(users)

print(users["1"].get("name"))
print(users["2"].get("email"))
print("### Inside nested dictionary loop")
for index in users:
    for key, value in users[index].items():
        print(key, value, sep=" : ")
    for user in users[index].values():
        print(user)
