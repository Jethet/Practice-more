# Create a function that returns True if an integer is divisible by 5,
# and false otherwise.

def divisible_by_five(n):
    if n % 5 == 0:
        return True
    else:
        return False

print(divisible_by_five(5)) #➞ True
print(divisible_by_five(-55)) #➞ True
print(divisible_by_five(37)) #➞ False
