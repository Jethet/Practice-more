# Create a function that takes a string and returns a string in which each
# character is repeated once.

def double_char(txt):
    return ''.join([x*2 for x in txt])

print(double_char("String")) # "SSttrriinngg"
print(double_char("Hello World!")) # "HHeelllloo  WWoorrlldd!!"
print(double_char("1234!_ ")) # "11223344!!__  "
