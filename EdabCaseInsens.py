# Write a function that validates whether two strings are identical.
# Make this validator case insensitive.

def match(s1, s2):
    return s1.lower() == s2.lower()

print(match("hello", "hELLo")) #➞ True
print(match("motive", "emotive")) #➞ False
print(match("venom", "VENOM")) #➞ True
print(match("mask", "mAskinG")) #➞ False
