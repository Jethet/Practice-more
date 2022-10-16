# Given a string, return the string made of its first two chars.
# If the string is shorter than 2, return whatever there is.

def first_two(str):
    return str[0:2]

print(first_two('Hello'))
print(first_two('X'))
print(first_two(''))
