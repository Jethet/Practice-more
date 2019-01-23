# Create a function that takes a number as an argument and returns True
# or False depending on whether the number is symmetrical or not. A number
# is symmetrical when it is the same as its reverse.

def is_symmetrical(num):
    x = str(num)
    return x == x[::-1]



print(is_symmetrical(7227)) # True

print(is_symmetrical(12567)) # False

print(is_symmetrical(44444444)) # True

print(is_symmetrical(9939)) # False

print(is_symmetrical(1112111)) # True
