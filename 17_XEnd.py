# Given a string, return a new string made of 3 copies of the last
# 2 characters of the original string (string length will be at least 2).

def extra_end(str):
    return 3 * str[-2:]

print(extra_end('Hello'))
