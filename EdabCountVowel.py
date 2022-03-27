# Create a function that takes a string and returns the number (count) of
# vowels contained within it.
# a, e, i, o, u are considered vowels (not y).
# All test cases are one word and only contain letters.

def count_vowels(txt):
    vowel = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for x in txt:
        if x in vowel:
            count += 1
    return count


print(count_vowels("Celebration")) # 5
print(count_vowels("Palm"))       # 1
print(count_vowels("Prediction")) # 4
