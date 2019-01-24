# Create a function that takes a single string as argument and returns an
# ordered list containing the indexes of all capital letters in the string.
# Return an empty array if no uppercase letters are found in the string.
# Special characters ($#@%) and numbers will be included in some test cases.

def indexOfCaps(word):
    caps_list = []
    for x in word:
        if x.isupper() == True:
            y = word.index(x)
            caps_list.append(y)
    return caps_list

print(indexOfCaps("eDaBiT")) # [1, 3, 5]

print(indexOfCaps("eQuINoX")) # [1, 3, 4, 6]

print(indexOfCaps("determine")) #[]

print(indexOfCaps("STRIKE")) # [0, 1, 2, 3, 4, 5]

print(indexOfCaps("sUn")) # [1]
