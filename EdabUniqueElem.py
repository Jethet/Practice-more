# Write a function that returns True if two arrays have the same number of
# unique elements, and false otherwise.

def same(a1, a2):
    return len(set(a1)) == len(set(a2))

print(same([1, 3, 4, 4, 4], [2, 5, 7])) #➞ True
print(same([9, 8, 7, 6], [4, 4, 3, 1])) #➞ False
print(same([2], [3, 3, 3, 3, 3])) #➞ True
