# Given a number n, write a function that returns PI to n decimal places.

import math

def my_pi(n):
    return round(math.pi, n)


print(my_pi(5)) # 3.14159
print(my_pi(4)) # 3.1416
print(my_pi(15)) # 3.141592653589793
