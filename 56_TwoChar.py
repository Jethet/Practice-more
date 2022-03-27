# Given a string, return a string in which every char in original is doubled.

def double_char(str):
    return ''.join(x*2 for x in str)

# from CodingBat:
def double_char(str):
    result = ""
    for i in range(len(str)):
        result += str[i] + str[i]
    return result

print(double_char('The'))
