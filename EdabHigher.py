# Write a function that returns True if there exists at least one number that
# is larger than or equal to n.
# Return False for an empty array []

def exists_higher(lst, n):
    return any(x >= n for x in lst)


print(exists_higher([5, 3, 15, 22, 4], 10)) #➞ True
print(exists_higher([1, 2, 3, 4, 5], 8)) #➞ False
print(exists_higher([4, 3, 3, 3, 2, 2, 2], 4)) #➞ True
print(exists_higher([], 5)) #➞ False
