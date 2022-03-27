# Given two strings and a character, create a function that returns the total
# number of unique characters from the combined string.

def count_unique(s1, s2):
    return len(set(s1 + s2))

print(count_unique("apple", "play")) #➞ 5
# "appleplay" has 5 unique characters:
# "a", "e", "l", "p", "y"
print(count_unique("sore", "zebra")) #➞ 7
print(count_unique("a", "soup")) #➞ 5
