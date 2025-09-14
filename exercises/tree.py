#1
numbers = (1,2,3,77,90)
print(f"First number: {numbers[0]} and Last number: {numbers[-1]}")
#2
ages = (10,20,30)
ages = list(ages)
ages.append(40)
ages = tuple(ages)
print(ages)
#3
fruits = ("apple", "banana", "apple", "cherry")
apples = [x for x in fruits if x == "apple"]
print(len(apples))
#4
fruits = {"apple", "banana", "apple", "cherry"}
print(fruits)
fruits.add('strawberry')
print(fruits)
fruits.remove('apple')
print(fruits)
#5
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Set one", set1,sep=': ')
print("Set two", set2,sep=': ')
set3 = set1.union(set2)
print("Set three", set3,sep=': ')
print("Intersection ",set1.intersection(set2))
print("Difference between one and two is ",set1.difference(set2))
#6
numbers = [1, 2, 2, 3, 4, 4, 5]
print(set(numbers))
#7
set_1 = {1, 2, 3, 4}
print(f"Is {1, 2} is a subset of {set_1}: ",{1, 2}.issubset(set_1))
#8
set_1 = {10, 20, 30}
print(f"Is {40, 50} is a disjoint of {set_1} ",set_1.isdisjoint({40, 50}))
#9
colors = {"red", "blue", "green"}
print(colors)
colors.discard('red')
colors.discard('yellow')
print(colors)
#10
team_1 = {'Real','Barca','Porto'}
team_2 = {'Palmer\'s','PSG','Barca','Real'}
team_1.intersection_update(team_2)
print(team_1)

## Practice exercise for sets

# 1
shop1 = {"alice@gmail.com", "bob@gmail.com", "claire@gmail.com"}
shop2 = {"david@gmail.com", "bob@gmail.com", "eve@gmail.com"}
unique_emails = shop1.union(shop2)
print(unique_emails)
# 2
insta_followers = {"ali", "fatima", "sami", "john"}
twitter_followers = {"john", "amina", "sami", "lina"}
print(insta_followers.intersection(twitter_followers))
# 3
registered = {"Ayan", "Zara", "Musa", "Omar"}
attended = {"Zara", "Musa"}
print(registered.difference(attended))