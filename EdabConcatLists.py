# Create a function to concatenate two integer lists.

def concat(lst1, lst2):
    return lst1 + lst2

print(concat([1, 3, 5], [2, 6, 8])) #➞ [1, 3, 5, 2, 6, 8]
print(concat([7, 8], [10, 9, 1, 1, 2])) #➞ [7, 8, 10, 9, 1, 1, 2]
print(concat([4, 5, 1], [3, 3, 3, 3, 3])) #➞ [4, 5, 1, 3, 3, 3, 3, 3]
