# Create a function that takes a single character as an argument and returns
# the char code of its lowercased / uppercased counterpart.
# Given that    - "A" char code is: 65    - "a" char code is: 97
# Not all inputs will have a counterpart (e.g. numbers),
# in which case return the inputs char code

def counterpartCharCode(char):
    char_new = char.swapcase()
    return ord(char_new)

print(counterpartCharCode("A")) # 97
print(counterpartCharCode("a")) # 65
