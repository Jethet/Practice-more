# Create function that takes list of numbers and returns the number that's unique.

def unique(lst):
	for x in lst:
		if lst.count(x) == 1:
			return x


print(unique([3, 3, 3, 7, 3, 3]))  # 7
print(unique([0, 0, 0.77, 0, 0])) # 0.77
print(unique([0, 1, 1, 1, 1, 1, 1, 1])) # 0
