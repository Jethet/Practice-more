# An isogram is a word that has no repeating letters, consecutive or nonconsecutive.
# Create a function that takes a string and returns either True or False
# depending on whether or not it's an "isogram".
# Ignore letter case (should not be case sensitive).

def is_isogram(txt):
    new_txt = txt.lower()
    for x in new_txt:
        if new_txt.count(x) > 1:
            return False
    return True

print(is_isogram("Algorism")) # True

print(is_isogram("PasSword")) # False (not case sensitive)

print(is_isogram("Consecutive")) # False
