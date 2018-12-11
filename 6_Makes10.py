#Given two ints a and b, return True if one of them is 10 or their sum is 10

def makes10(a, b):
    if a == 10 or b == 10:
        return True
    if a + b == 10:
        return True
    else:
        return False

#solution CodingBat:
def makes10(a, b):
    return (a == 10 or b== 10 or a+b == 10)
