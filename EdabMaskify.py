# Usually when you sign up for an account to buy something, your credit card
# number, phone number or answer to a secret question is partially obscured
# in some way. Since someone could look over your shoulder, you don't want that
# shown on your screen. Hence, the website masks these strings.
# Your task is to create a function that takes a string, transforms all but
# the last four characters into "#" and returns the new masked string.
# The maskify function must accept a string of any length and if it is an empty
# string it should return an empty string (fourth example).

def maskify(txt):
    if len(txt) == 0:
        return ''
    if len(txt) < 4:
        return txt
    if len(txt) >= 4:
        new_txt1 = txt[0:-4]
        new_txt2 = txt[-4::]
        return ('#' * len(new_txt1)) + new_txt2



print(maskify("4556364607935616")) # "############5616"

print(maskify("64607935616")) # "#######5616"

print(maskify("1")) # "1"

print(maskify("")) # ""
