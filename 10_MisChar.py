#Given a non-empty string and int n, return new string where the char at
# index n has been removed. The value of n will be a valid index of a
# char in the original string (i.e.: n will be in range 0..len(str) - 1)

def missing_char(str, n):
    nwstr = str[:n] + str[n+1:]
    return nwstr

print(missing_char('kitten', 1))
