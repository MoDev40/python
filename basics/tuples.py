my_tuple = ('apple','banana','orange','apple')
print(my_tuple)
print(len(my_tuple))
print(my_tuple[0])

one_item_tuple = ('onion',)
print(type(one_item_tuple))

tuple1 = tuple(('Mellon','Banana'))
tuple2 = (True,False)
tuple3 = (1,3,4,5)
print(tuple1)
print(tuple2)
print(tuple3)

items = ('Iphone 11','A10','A75','Xiaomi','Huawei')
print(items)
x = list(items)
x.append('hp')
x.remove('Iphone 11')
items = tuple(x)
print(items)

# Unpacking

(a10,a75,xiaomi,huawei,hp) = items
print(a10)
print(a75)
print(xiaomi)
print(huawei)

(a10,a75,*etc) = items

print(a10)
print(a75)
print(etc)

(a10,*etc,_hp) = items
print(a10)
print(etc)
print(_hp)

multiplied = items * 2
print(multiplied)

print(multiplied.index('Huawei'))
print(items.index('hp'))

print(len(items))