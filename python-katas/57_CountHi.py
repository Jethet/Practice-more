# Return the number of times the string 'hi' appears in a given string.

def count_hi(str):
    return str.count('hi')

# CodingBat solution:
def count_hi(str):
    sum = 0
    for i in range(len(str)-1):
        if str[i:i+2] == 'hi':
            sum += 1      #or: sum = sum + 1
    return sum

print(count_hi('abc hi ho'))
print(count_hi('ABChi hi'))
print(count_hi('hihi'))
