# Given three ints, a b c, return True if one of b or c is "close" (differing
# from a by at most 1), while the other is "far", differing from both other
# values by 2 or more. Note: abs(num) computes the absolute value of a number.

def close_far(a, b, c):
    if b - a <= abs(1) and c - a >= abs(2) and c - b >= abs(2):
        return True
    if c - a <= abs(1) and b - a >= abs(2) and b - c >= abs(2):
        return True
    else:
        return False

print(close_far(1, 2, 10)) # True
print(close_far(1, 2, 3))  # False
print(close_far(4, 1, 3))  # True
print(close_far(8, 6, 9))  # True
print(close_far(10, 10, 8))  # True
