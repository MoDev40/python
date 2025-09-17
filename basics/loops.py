for i in range(5):
    print(f"The iteration {i+1} of 5")

# a = True
# while a:
# 	print('continue')
# 	res = input('Do you want to continue? (y/n) ').strip().lower()
# 	if res == 'n':
# 		a = False
# 	else:
# 		a = True

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(f"This fruit is {fruit.title()}")

json = [
    dict(name="John Doe", age=25, city="New York"),
    dict(name="Jane Doe", age=19, city="Orlando"),
]

for item in json:
    print(
        f"My name is {item['name']} and i'm {item['age']} years old now i'm in {item['city']}."
    )


i = 1
while i <= 6:
    print(i)
    i += 1
    if i == 2:
        continue
else:
    print("The end of the loop")


for x in range(5):
    print(x)

for x in range(2, 7):
    print(x)

for x in range(0, 10, 2):
    print(x)
else:
    print("we are on destination.")

for x in range(6):
    print(x)
    if x == 4:
        break
else:
    print("Finally ended")

colors = ["red", "green", "blue"]
mixed_colors = ["red", "green", "blue", "yellow"]

for color in colors:
    print(color)
    for mixed_color in mixed_colors:
        print(color, mixed_color, sep=" , ")

for x in [1, 2, 3]:
    pass
