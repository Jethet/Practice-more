#Given 2 int values return True if one is neg and one is positive.
#Third parameter is 'negative': if 'negative' is True and two values
#are both negative, return True.

def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    else:
        return a < 0 and b > 0 or a > 0 and b < 0

print(pos_neg(3, -4, False))
print(pos_neg(3, -4, True))
print(pos_neg(3, 4, False))
print(pos_neg(3, 4, True))
print(pos_neg(-3, -4, False))
print(pos_neg(-3, -4, True))
