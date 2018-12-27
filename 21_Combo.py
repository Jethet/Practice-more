# Given two strings a and b, return string in format short+long+short,
# with the shorter string on the outside and longer string in the middle.

def combo_string(a, b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b

print(combo_string('hello', 'hi'))
