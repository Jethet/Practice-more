# Create a function that takes a string, checks if it has the same number
# of 'x's and 'o's and returns either True or False.
#  - Return a boolean value (True or False).
#  - The string can contain any character.
#  - When no x and no o are in the string, return True.

# Remember to return True if no x's or o's; must be case insensitive.

def x_o(txt):
    new_txt = txt.lower()
    if new_txt.count('x') == new_txt.count('o'):
        return True
    elif 'x' not in new_txt and 'o' not in new_txt:
        return True
    else:
        return False


print(x_o("ooxx"))   # True
print(x_o("xooxx"))  # False
print(x_o("ooxXm"))  # True (case insensitive)
print(x_o("zpzpzpp")) # True (returns true if no x and o)
print(x_o("zzoo"))   # False
