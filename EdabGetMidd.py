# Create a function that takes a string and returns the middle character(s).
# If the word's length is odd, return the middle character. If the word's
# length is even, return the middle two characters.

def get_middle(word):
    try:
        if len(word) % 2 == 1:
            mid = round(len(word)/2)
            return word[mid-1]
    except:
        return word[mid]

    else: #len(word) % 2 == 0:
        mid = round(len(word)/2)
        return word[mid-1] + word[mid]


print(get_middle("test")) # "es"
print(get_middle("testing")) # "t"
print(get_middle("middle")) # "dd"
print(get_middle("A")) # "A"
