# Given a string of even length, return the first half.

def first_half(str):

    return str[:len(str)/2]


print(first_half('WooHoo'))

# This is very strange: the code generates an error in Atom but
# not in the CodingBat IDE: it runs fine.
