# A palindrome is a word, phrase, number or other sequence of characters which
# reads the same backward or forward, such as madam or kayak.
# Write a function that takes a string and determines whether it's a palindrome
# or not. The function should return a boolean (True or False value).
# Should be case insensitive and special characters (punctuation or spaces)
# should be ignored.

import string

def is_palindrome(txt):
    exclude = set(string.punctuation)
    txt = ''.join(ch for ch in txt if ch not in exclude).replace(' ','').lower()
    #print(txt)
    return txt == txt[::-1]


print(is_palindrome("A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!")) # True
print(is_palindrome("Neuquen")) # True
print(is_palindrome("Not a palindrome")) # False
