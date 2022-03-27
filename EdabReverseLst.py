# Write a function to reverse a list.

def reverse(lst):
    return lst[::-1]


print(reverse([1, 2, 3, 4])) #➞ [4, 3, 2, 1]
print(reverse([9, 9, 2, 3, 4])) #➞ [4, 3, 2, 9, 9]
print(reverse([])) #➞ []
