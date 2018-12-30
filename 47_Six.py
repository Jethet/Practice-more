# Given two int values, a and b, return True if either one is 6, or if
# their sum or difference is 6 (the function abs(num) computes absolute value)

def six(a, b):
    if abs(a) == 6:
        return True
    elif abs(b) == 6:
        return True
    elif abs(a + b) == 6:
        return True
    elif abs(a - b) == 6:
        return True
    elif abs(b - a) == 6:
        return True
    else:
        return False

print(six(6, 4))
print(six(4, 5))
print(six(1, 5))
print(six(7, 2))
