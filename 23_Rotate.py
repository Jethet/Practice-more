# Given a string, return a 'rotated left 2' version where the first 2 chars
# are moved to the end.

def left2(str):
    x = str[0:2]
    return str[2:] + x

print(left2('hello'))
