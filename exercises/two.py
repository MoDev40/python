# 1
numbers = list((1, 2, 3, 4, 5))
print(numbers)
ages = [16, 11, 27, 30]
print(ages)

#2
my_list = ["apple", "banana", "cherry"]
print(my_list[1])  # banana

# 3
print(len(my_list))

# 4
fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.append("orange")
print(fruits)

# 5
"""
	append adds an item to the end of the list
	extend adds existing items to the end of the list
"""
fruits.append("onion")
print(fruits)
fruits.extend(list(('rose','watermelon')))
print(fruits)

# 6
numbers = [10, 20, 30, 40, 50]
print(numbers)
numbers[2] = 35
print(numbers)

# 7
fruits = ["apple", "banana", "cherry", "banana"]
del fruits[1]
print(fruits)
fruits.remove('apple')
print(fruits)
fruits.pop()
print(fruits)

# 8
nums = [5, 2, 9, 1, 7]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

# 9
colors = ["red", "green", "blue"]
print(colors)
colors.insert(1,'yellow')
print(colors)

# 10
basket = ["mango", "apple", "grape"]

if 'apple' in basket:
	print('Apple is in the basket')
	
# 11
data = [[1, 2], [3, 4], [5, 6]]
print(data)
print(data[1][0] + data[-1][-1])
"""
9 Because it nested array when data[1] you got [3, 4] because of the index and when you say [0] you go 3
that was data[1][0] which is 3
When you say data[-1] you got last index item which is list of [5, 6] and the you say [-1] again you got the last which is 6
so data[-1][-1] you got 6 then add we got 9 that is why.
"""

# 12

even_numbers_squares = [x**2 for x in range(1,11) if x % 2 == 0]
print(even_numbers_squares)

# 13

items = ["apple", "banana", "apple", "orange", "banana", "grape"]
print(items)

items_without_duplicate = []
for item in items:
	if item not in items_without_duplicate:
		items_without_duplicate.append(item)

print(items_without_duplicate)

# 14
nums = [3, 8, -2, 5, -7, 10, 0, -1]
print(nums)
positive_multiplied_by_two = [ x * 2 for x in nums if x > 0 ]
print(positive_multiplied_by_two)

# 15
letters = ["a", "b", "a", "c", "b", "a", "d", "b"]

letter_counter = dict()

for letter in letters:
	if letter not in letter_counter:
		letter_counter[letter] = 1
	else:
		letter_counter[letter] += 1
print(letter_counter)