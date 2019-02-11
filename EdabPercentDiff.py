# Create a function that takes two numbers as arguments and return the percent
# difference between them.

def percent_diff(num1, num2):
    value = (num1 - num2) / ((num1 + num2) / 2) * 100
    return abs(round(value, 1))

print(percent_diff(60, 100)) #➞ 50.0

print(percent_diff(100, 60)) #➞ 50.0

print(percent_diff(4538, 5439)) #➞ 18.1

print(percent_diff(4538, 5439)) #➞ 18.1
