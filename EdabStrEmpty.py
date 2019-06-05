# Create a function that returns True if a string is empty and False otherwise.

def is_empty(s):
    if len(s) == 0:
        return True
    else:
        return False

print(is_empty("")) #➞ True
print(is_empty(" ")) #➞ False
print(is_empty("a")) #➞ False
