# Given a string, return the count of the number of times that a substring
# length 2 appears in the string and also as the last 2 chars of the string,
# so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
    x = str[-2:]
    return str.count(x) - 1

print(last2('axxxaaxx'))
