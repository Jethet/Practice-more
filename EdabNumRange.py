# Given a number and a dictionary with min and max properties, return True if
# the number lies within the given range (inclusive).
# Numbers can be positive or negative, and they may not be integers.
# You can assume min <= max is always true.

def is_in_range(n, r):
    x = r.values()
    y = list(x)
    return n >= y[0] and n <= y[1]

print(is_in_range(4, { "min": 0, "max": 5 })) #➞ True
print(is_in_range(4, { "min": 4, "max": 5 })) #➞ True
print(is_in_range(4, { "min": 6, "max": 10 })) #➞ False
print(is_in_range(5, { "min": 5, "max": 5 })) #➞ True
