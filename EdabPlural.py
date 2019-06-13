# Create a function that takes in a word and determines whether or not it is
# plural. A plural word is one that ends in "s".

def is_plural(word):
    return word[-1] == 's'

print(is_plural("changes")) #➞ True
print(is_plural("change")) #➞ False
print(is_plural("dudes")) #➞ True
print(is_plural("magic")) #➞ False
