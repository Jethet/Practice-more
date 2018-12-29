# Given 2 ints, a and b, return their sum. Sums in the range 10..19 inclusive,
# are forbidden, so in that case just return 20.

def sorta_sum(a, b):
    c = a + b
    if c >= 10 and c <= 19:
        return 20
    else:
        return c

print(sorta_sum(3, 4))
print(sorta_sum(9, 4))
print(sorta_sum(10, 11))
