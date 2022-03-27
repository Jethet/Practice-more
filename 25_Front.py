# Given a string and a non-negative int n, the front of the string is the
# first 3 chars, or whatever is there if the string is less than length 3.
# Return n copies of the front.

def front_times(str, n):
    return str[0:3] * n

print(front_times('hello', 4))
