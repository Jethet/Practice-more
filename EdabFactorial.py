# Create a function that takes an integer and returns the factorial of that
# integer. That is, the integer multiplied by all positive lower integers.

def factorial(num):
    result = 1
    for x in range(2, num+1):
        result *= x
    return result






print(factorial(3)) # 6
print(factorial(5)) # 120
print(factorial(13)) # 6227020800

"""
FACTORIAL:

n! = n × (n−1)!

--- this means:

the factorial of any number is that number times
the factorial of (that number minus 1)

So 10! = 10 × 9!, ... and 125! = 125 × 124!, etc.
"""
