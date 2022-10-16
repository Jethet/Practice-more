# Create a function that takes an integer and returns True if it's divisible
# by 100, otherwise return False.


def divisible(num):
    return num % 100 == 0



print(divisible(1)) # False
print(divisible(1000)) # True
print(divisible(100)) # True
