# Create a function that returns True if a string contains any spaces.

def has_spaces(txt):
    x = " "
    return x in txt


print(has_spaces("hello")) #➞ False
print(has_spaces("hello, world")) #➞ True
print(has_spaces(" ")) #➞ True
print(has_spaces("")) #➞ False
print(has_spaces(",./!@#")) #➞ False
