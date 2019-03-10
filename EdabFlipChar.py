# Create a function that takes a string and returns a new string with its first
# and last characters swapped, except under three conditions:
#    If the length of the string is less than two, return "Incompatible.".
#    If the argument is not a string, return "Incompatible.".
#    If the first and last characters are the same, return "Two's a pair.".
# Tests are case sensitive (e.g. "A" and "a" are not the same character).

def flip_end_chars(txt):
    if len(txt) < 2:
        return "Incompatible."
    elif type(txt) is list:
    #elif txt.isalpha() != True:
        return "Incompatible."
    elif txt[0] == txt[-1]:
        return "Two's a pair."
    else:
        return txt[-1] + txt[1:-1] + txt[0]



print(flip_end_chars("Cat, dog, and mouse.")) # ".at, dog, and mouseC"
print(flip_end_chars("ada")) # "Two's a pair."
print(flip_end_chars("Ada")) # "adA"
print(flip_end_chars("z")) # "Incompatible."
print(flip_end_chars([1, 2, 3])) # "Incompatible."
