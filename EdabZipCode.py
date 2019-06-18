# Zip codes consist of 5 consecutive digits. Given a string, write a function
# to determine whether the input is a valid zip code.
# Valid zip codes should not be any spaces between the digits.

def is_valid(zip_code):
    return zip_code.isdecimal() and ' ' not in zip_code

print(is_valid("59001")) #➞ True
print(is_valid("853a7")) #➞ False
print(is_valid("732 32")) #➞ False
