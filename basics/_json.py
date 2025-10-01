from datetime import datetime as dt
from json import loads, dumps

user = '{ "name":"John", "age":30, "city":"New York"}'
data = loads(user)
print(data.get("name"))

data["updated_at"] = dt.now().strftime("%Y-%m-%d %H:%M:%S")

print(type(dumps(data)))
print(dumps(data))

details = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}],
}

print(dumps(details, indent=4, sort_keys=True))
print(dumps(True))
print(dumps("Hi"))
print(loads("true"))
