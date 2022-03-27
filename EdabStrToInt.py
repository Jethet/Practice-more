#Write two functions:
#    to_int() : A function to convert a string to an integer.
#    to_str() : A function to convert an integer to a string.

def to_int(str):
    return int(str)

print(to_int("77")) # 77
print(to_int("532")) # 532

def to_str(int):
    return str(int)

print(to_str(77)) # "77"
print(to_str(532)) # "532"
