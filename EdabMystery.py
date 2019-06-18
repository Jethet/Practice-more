# This is a reverse coding challenge. Your task is to create a function that,
# when fed the inputs below, produce the sample outputs shown.

def mystery_func(lst, n):
    return [num % n for num in lst]

print(mystery_func([5, 7, 8, 2, 1], 2)) #➞ [1, 1, 0, 0, 1]
print(mystery_func([9, 8, 16, 47], 4)) #➞ [1, 0, 0, 3]
print(mystery_func([17, 11, 99, 55, 23, 1], 5)) #➞ [2, 1, 4, 0, 3, 1]
print(mystery_func([6, 1], 7)) #➞ [6, 1]
print(mystery_func([3, 2, 9], 3)) #➞ [0, 2, 0]
print(mystery_func([48, 22, 0, 19, 33, 100], 10)) #➞ [8, 2, 0, 9, 3, 0]
