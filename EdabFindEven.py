# Using list comprehensions, create a function that finds all even numbers
# from 1 to the given number.

def find_even_nums(num):
	return [i for i in range(1, num+1) if i % 2 == 0]





print(find_even_nums(8)) # [2, 4, 6, 8]
print(find_even_nums(4)) # [2, 4]
print(find_even_nums(2)) # [2]

"""
Try to use list comprehensions in your solution. Here's an example:

vals = [expression
	for value in collection
		if condition]

This is equivalent to:

vals = []
for value in collection:
	if condition:
		vals.append(expression)
"""
