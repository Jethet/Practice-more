# Create a function that accepts a list of two strings and checks if the letters
# in the second string are present in the first string. Function should not be
# case sensitive (as indicated in the second example).
# Both strings are presented as a single argument in the form of a list.

def letter_check(lst):
    lst1 = lst[0]
    lst2 = lst[1]
    lst1 = lst1.lower()
    lst2 = lst2.lower()
    for char in lst2:
        if char not in lst1:
            return False
    else:
        return True

print(letter_check(["trances", "nectar"])) # True
print(letter_check(["compadres", "DRAPES"])) # True
print(letter_check(["parses", "parsecs"])) # False
