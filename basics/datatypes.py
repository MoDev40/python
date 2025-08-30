# x = int(100)
# y = float(20.0)
# left = complex(2j)
# countries = list(('Somalia','Yemen','Falestiin'))
# cities = tuple(('Mogadisho','London'))
# count = range(10)
# json = dict(name="Mdev",age=33)
# fruits = set(('Mango','Apple'))
# freezset = frozenset(('Freeze','Cold'))
# istrue = bool(False)
# byte_array = bytearray(10)
# string = str('Mdev')
#
# print(countries)
# print(cities)
# print(count)
# print(json)
# print(fruits)
# print(freezset)
# print(istrue)
# print(byte_array)
# print(string)
#
#
# teams = ['Man City','Barca','PSG']
# print(teams)
#
# players = ('Ryan','Pedri','Pacho')
# print(type(players))
#
# coaches = [{'name':'Josep','age':54},{'name':'Gasperini','age':74}]
# print(coaches)
# coaches.append({'name':'Jose','age':54})
# print(coaches)
# refs = frozenset(('Ryan','Pedro','Paco'))
# print(refs)
# print(type(refs))
from itertools import count

# String

vehicle = "Tesla"
print(vehicle)

multiline = """Once a time there is a such a young age boy who doesn't need anymore to stay along life. """
print(multiline)

print(vehicle[0])

for x in vehicle:
	print(x)

print(len(vehicle))

print("T" in vehicle)

print("V" not in vehicle)

vehicle += ',Its time to buy'

print(vehicle[2:4])
print(vehicle[2:])
print(vehicle[:3])
print(vehicle.isupper())
print(vehicle.lower())
print(vehicle.title())
print(vehicle.strip())
print(vehicle.split(','))

print(f"The price of this phone is around ${1500:.2f} dollars")
print(f"My name is {vehicle.split(',')[0].title()} and I am modern vehicles")

print("can i get this little \"toy\".")
print("So far so good \tMove away")
print("So much love new lines \nHi")
print("What is mean\\")
print("What return can do for me \rHello where the previous line.😒")

define_age = "Can we just say age isn\'t number"
print(define_age.count('we'))
print(define_age.encode())
print(define_age.isnumeric())
print(define_age.isalnum())
print(define_age.isalpha())
print(define_age.isascii())