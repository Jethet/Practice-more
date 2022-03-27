#Given a string, return a new string with 'not' added to the front.
#If string begins with 'not', return the string unchanged.

def not_string(string):
    if string[0:3] == 'not':
        return string
    else:
        return "not " + string

print(not_string('candy'))
print(not_string('notable'))
