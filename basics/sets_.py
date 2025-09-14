team = {'SYL','Raashid','Simba','Aargo'}
print(team)
print(type(team))

fruits = {'apple','banana','orange','apple','mango'}
print(fruits)

"""
	The values True and 1 also False and 0 are considered the same value in sets, and are treated as duplicates
"""

my_set = {True,False,0,1,2,'Done'}
print(my_set)

print(len(my_set))

for fruit in fruits:
	print(fruit)

print('apple' in fruits)
print('watermelon' not in fruits)

print(fruits)

fruits.add('strawberry')
print(fruits)
fruits.update(team)
print(fruits)
team.update(['Barca','Nice'])
print(team)
# team.remove('real')
team.discard('real')
x=team.pop()
print(x)
print(team)
team.remove('Barca')
team.discard('Nice')
print(team)
team.clear()
print(team)
# del team

# Set Joining....

set_1 = {1, 2, 3, 4, 5}
set_2 = {'Python', 'Java','Ruby'}
print(set_1)
print(set_2)
set_3 = set_1.union(set_2)
print(set_3)
set_4 = set_1 | set_2
print(set_4)
set_5 = set_1.union(set_2,set_3,set_4,{'Go','TS'})
print(set_5)
print(set_5.union(['PHP','JS']))

set1 = {"a", "b" , "c"}
set2_ = {1, 2, 3}

set1.update(set2_)
print(set1)
