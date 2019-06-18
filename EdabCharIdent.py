# Write a function that returns True if all characters in a string are identical
# and False otherwise.

def is_identical(s):
    return len(set(s)) == 1

print(is_identical("aaaaaa")) #➞ True

print(is_identical("aabaaa")) #➞ False

print(is_identical("ccccca")) #➞ False

print(is_identical("kk")) #➞ True
