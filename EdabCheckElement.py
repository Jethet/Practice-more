# Write a function to check whether a list contains a particular element.

def check(lst, el):
    return el in lst



print(check([1, 2, 3, 4, 5], 3)) # True
print(check([1, 1, 2, 1, 1], 3)) # False
print(check([5, 5, 5, 6], 5)) # True
print(check([], 5)) # False
