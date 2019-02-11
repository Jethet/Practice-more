# Create a function that takes a string and returns the middle character(s).
# If the word's length is odd, return the middle character. If the word's length
# is even, return the middle two characters.

def get_middle(word):
    if len(word) % 2 == 1:
        mid = len(word)/2
        return mid
        #return word[mid]
    #if len(word) % 2 == 0:
        #mid = len(word)/2
        #return word[mid] + word[mid+1]

print(get_middle('whatevery'))

#print(get_middle("test")) #➞ "es"
#print(get_middle("testing")) #➞ "t"
#print(get_middle("middle")) #➞ "dd"
#print(get_middle("A")) #➞ "A"
