mylist = [1, 2, 3, 4]
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(mylist)

print(len(mylist))

print(mylist[0])
print(fruits[0])
print(fruits[:2])

duplicateList = [1, 11, 1, 2, 1, 67]
print(duplicateList)
duplicateList.append(7)
print(duplicateList)

fruits[0] = "Onion"
print(fruits)

mixedList = ["apple", True, 5]
print(mixedList)

print(type(mixedList))

print(list(("Oil", "Gasoline", "Gear")))

print(fruits[-1])

fruits.extend(["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"])
print(fruits)
print(fruits[2:5])
print(fruits[:6])
print(fruits[1:])
print(fruits[-4:-2])

if "apple" in fruits:
    print("Yes apple is in the fruits list")


fruits[3] = "blackcurrant"
fruits[:3] = ["cheese", "milk"]
print(fruits)

items = ["mobile", "laptop", "vanilla"]
print(items)
items[1:2] = ["guest", "noodle"]
print(items)

test = ["apple", "banana", "cherry"]
print(test)

test.append("Onion")
print(test)
test.insert(2, "watermelon")
print(test)
test.extend(["Lemon", "orange"])
print(test)
test.extend(list(("Cucumber", "Green Lemon")))
print(test)
test.remove("orange")
print(test)
test.pop()
print(test)
test.pop(1)
print(test)
del test[0]
print(test)
test.clear()
print(test)
del test

for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    print(fruits[i])

i = 0

print("Using while loop")
while i < len(fruits):
    print(fruits[i])
    i += 1

print("Using list comprehension")
[print(x) for x in fruits]

newList = []
for x in fruits:
    if "a" in x:
        newList.append(x)

print(newList)

newList = [x for x in fruits if "b" in x]

print(newList)

odd_numbers = [x for x in range(20) if x % 2 == 0]
print(odd_numbers)
even_numbers = [x for x in range(20) if x % 2 == 1]
print(even_numbers)

numbers = [x if x >= 5 else x % 2 for x in range(20)]
print(numbers)

l1 = ["apple", "banana", "cherry"]
print(l1)
l2 = l1
l3 = l1.copy()
print(l2)
l1.append("orange")
print(l2)
print(l3)
