x = int(100)
y = float(20.0)
left = complex(2j)
countries = list(('Somalia','Yemen','Falestiin'))
cities = tuple(('Mogadisho','London'))
count = range(10)
json = dict(name="Mdev",age=33)
fruits = set(('Mango','Apple'))
freezset = frozenset(('Freeze','Cold'))
istrue = bool(False)
byte_array = bytearray(10)
string = str('Mdev')

print(countries)
print(cities)
print(count)
print(json)
print(fruits)
print(freezset)
print(istrue)
print(byte_array)
print(string)


teams = ['Man City','Barca','PSG']
print(teams)

players = ('Ryan','Pedri','Pacho')
print(type(players))

coaches = [{'name':'Josep','age':54},{'name':'Gasperini','age':74}]
print(coaches)
coaches.append({'name':'Jose','age':54})
print(coaches)
refs = frozenset(('Ryan','Pedro','Paco'))
print(refs)
print(type(refs))