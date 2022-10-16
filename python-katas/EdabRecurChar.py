# Create a function that accepts a string as an argument and returns the first
# non-repeated character.
# An empty string should return False.
# If every character repeats, return False.

def first_non_repeated_character(txt):
    for char in txt:
        if txt.count(char) == 1:
            return char
    if txt == '':
        return False
    for char in txt[0::]:
        if txt.count(char) == 2:
            return False


print(first_non_repeated_character("it was then the frothy word met the round night")) #➞ "a"
print(first_non_repeated_character("the quick brown fox jumps then quickly blows air")) #➞ "f"
print(first_non_repeated_character("g")) #➞ "g"
print(first_non_repeated_character("")) #➞ False
print(first_non_repeated_character("hheelloo")) #➞ False
