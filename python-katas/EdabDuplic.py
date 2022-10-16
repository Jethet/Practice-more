# Create a function that takes a list of items, removes all duplicate items
# and returns a new list in the same sequential order as the old list
# (minus duplicates). Test cases contain lists with both strings and numbers.
# Case sensitive.

def removeDups(lst):
	new_lst = []
	for x in lst:
		if x not in new_lst:
			new_lst.append(x)
	return new_lst



print(removeDups(["John", "Taylor", "John"])) # ["John", "Taylor"]

print(removeDups([1, 0, 1, 0])) # [1, 0]

print(removeDups(['The', 'big', 'cat'])) # ['The', 'big', 'cat']
