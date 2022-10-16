# There is a single operator in Python capable of providing the remainder of a
# division operation. Two numbers are passed as parameters. The first provider
# divided by the second parameter will have a remainder, possiby zero. Return that value.

def remainder(x,y):
    return x % y


print(remainder(1, 3)) # 1
print(remainder(5, 5)) # 0
print(remainder(7, 2)) # 1
