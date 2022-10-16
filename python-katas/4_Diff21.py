#Given int n, return absolute difference between n and 21, except
#  if n is over 21: then return double the absolute difference

def diff21(n):
    if n <= 21:
        return abs(21-n)
    if n > 21:
        return 2 * (abs(n-21))

print(diff21(17))
print(diff21(61))
