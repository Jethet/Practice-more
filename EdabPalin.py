# A palindrome is a word, phrase, number or other sequence of characters which
# reads the same backward or forward, such as madam or kayak.
# Write a function that takes a string and determines whether it's a palindrome
# or not. The function should return a boolean (True or False value).
# Should be case insensitive and special characters (punctuation or spaces)
# should be ignored.

def is_palindrome(txt):
    punct = ['"', ' ', ',', '.', ';', '?', "'", '!', ':']
    for x in txt:
        if x in punct:
            new_txt = txt.replace(x, '')
    return(new_txt)
    print(new_txt)
    #txt2 = txt[::-1].islower()
    #print(txt, txt2)
    #return txt == txt2


print(is_palindrome("A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!")) # True
print(is_palindrome("Neuquen")) # True
print(is_palindrome("Not a palindrome")) # False
