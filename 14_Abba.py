# Given two strings a and b, return the result of putting them together
# in the order a b b a.

def make_abba(a, b):
    return a + b + b + a

a = 'Hi'
b = 'Bye'
print(make_abba(a, b))
