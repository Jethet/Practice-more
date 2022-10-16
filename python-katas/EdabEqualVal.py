# Write a function named equal that takes three input values (a, b, c) and
# returns the number of equal values. Your function must return 0, 2 or 3.

def equal(a, b, c):
    count = 0
    if a == b and b == c and a == c:
        count = 3
    elif a == b or b == c or a == c:
        count = 2
    else:
        count = 0
    return count


print(equal(3, 4, 3)) # 2

print(equal(1, 1, 1)) # 3

print(equal(3, 4, 1)) # 0
