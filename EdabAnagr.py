# Write a function that takes two strings and returns (True or False) whether
# they're anagrams or not. Should be case-insensitive.

def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())




print(is_anagram("cristian", "Cristina")) # True
print(is_anagram("Dave Barry", "Ray Adverb")) # True
print(is_anagram("Nope", "Note")) # False
