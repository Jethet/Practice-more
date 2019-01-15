# Create a function that takes two strings and returns True if the first
# argument ends with the second argument; otherwise return False.
#     Rules: Take two strings as arguments.
#            Determine if the second string matches ending of the first string.
#            Return boolean value.

def check_ending(str1, str2):
    if str1.endswith(str2):
        return True
    else:
        return False
        

print(check_ending("abc", "bc"))    # True
print(check_ending("abc", "d"))     # False
print(check_ending("samurai", "zi")) # False
print(check_ending("feminine", "nine")) # True
print(check_ending("convention", "tio")) # False
