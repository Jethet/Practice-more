# Create a function that takes a string, removes all "special" characters
# (e.g. ! @ # $ % ^ & \ *) and returns the new string.
# The only non-alphanumeric characters allowed are dashes -, underscores _ and spaces.

def remove_special_characters(txt):
    for x in txt:
        if x in ['!', '@', '#', '$', '^', '&', '*', '\\']:
            return txt.replace(x, '')



print(remove_special_characters("The quick brown fox!")) # "The quick brown fox"
print(remove_special_characters("%fd76$fd(-)6GvKlO.")) # "fd76fd-6GvKlO"
print(remove_special_characters("D0n$c sed 0di0 du1")) # "D0nc sed 0di0 du1"
