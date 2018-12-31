# Given three ints, a b c, return True if one of b or c is "close" (differing
# from a by at most 1), while the other is "far", differing from both other
# values by 2 or more. Note: abs(num) computes the absolute value of a number.

def close_far(a, b, c):
    if abs(b) - a <= 1 and abs(c) - a >= 2:
        return True
    elif abs(c) - a <= 1 and abs(b) - a >= 2:
        return True
    else:
        return False

print(close_far(1, 2, 10)) # True
print(close_far(1, 2, 3))  # False
print(close_far(4, 1, 3))  # True
