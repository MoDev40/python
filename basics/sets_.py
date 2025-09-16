team = {"SYL", "Raashid", "Simba", "Aargo"}
print(team)
print(type(team))

fruits = {"apple", "banana", "orange", "apple", "mango"}
print(fruits)

"""
	The values True and 1 also False and 0 are considered the same value in sets, and are treated as duplicates
"""

my_set = {True, False, 0, 1, 2, "Done"}
print(my_set)

print(len(my_set))

for fruit in fruits:
    print(fruit)

print("apple" in fruits)
print("watermelon" not in fruits)

print(fruits)

fruits.add("strawberry")
print(fruits)
fruits.update(team)
print(fruits)
team.update(["Barca", "Nice"])
print(team)
# team.remove('real')
team.discard("real")
x = team.pop()
print(x)
print(team)
team.remove("Barca")
team.discard("Nice")
print(team)
team.clear()
print(team)
# del team

# Set Joining....

set_1 = {1, 2, 3, 4, 5}
set_2 = {"Python", "Java", "Ruby"}
print(set_1)
print(set_2)
set_3 = set_1.union(set_2)
print(set_3)
set_4 = set_1 | set_2
print(set_4)
set_5 = set_1.union(set_2, set_3, set_4, {"Go", "TS"})
print(set_5)
print(set_5.union(["PHP", "JS"]))

set1 = {"a", "b", "c"}
set2_ = {1, 2, 3}

set1.update(set2_)
print(set1)

set1 = {"apple", "banana", "mango"}
set2 = {"apple", "banana", "orange"}
print(set1.intersection(set2))
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print(set1 & set2)

set1.intersection_update(set2)
print(set1)

set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

print(set1.difference(set2))
print(set2 - set1)

set2.difference_update(set1)
print(set2)
set1 = {"apple", "banana", "cherry", "onion"}
set2 = {"google", "microsoft", "apple", "onion"}
print(set2 ^ set1)

team1 = {"Paris", "Barca", "Real", "Arsenal"}
team2 = {"Man city", "Celtic", "Porto", "Arsenal"}

print(team1.union(team2))  # Joining
print(team1.intersection(team2))  # Keep duplicate
print(
    team1.difference(team2)
)  # Returns difference between while removing the elements that are in both.
print(team2.difference(team1))  # Returns difference between
print(
    team1.symmetric_difference(team2)
)  # appends both while removing the elements that are in both.
print(team2.symmetric_difference(team1))
