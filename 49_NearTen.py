# Given a non-negative number "num", return True if num is within 2 of a
# multiple of 10. Note: (a % b) is the remainder of dividing a by b (7 % 5 is 2).

def near_ten(num):
    x = num % 10
    if x >= 8 or x <= 2:
        return True
    else:
        return False


print(near_ten(12))
print(near_ten(17))
print(near_ten(19))
