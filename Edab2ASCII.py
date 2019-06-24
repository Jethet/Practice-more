# Return True if the sum of ASCII values of the first string is same as the sum
# of ASCII values of the second string, otherwise return False.

def same_ascii(a, b):
    return sum([ord(c) for c in a]) == sum([ord(c) for c in b])

print(same_ascii("a", "a")) #➞ True

print(same_ascii("AA", "B@")) #➞ True

print(same_ascii("EdAbIt", "EDABIT")) #➞ False
