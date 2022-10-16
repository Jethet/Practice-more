# Create a function that takes a list and returns the difference between the
# smallest and biggest numbers.

def difference_max_min(lst):
    return max(lst) - min(lst)

print(difference_max_min([10, 4, 1, 4, -10, -50, 32, 21])) #➞ 82
# Smallest number is -50, biggest is 32.
print(difference_max_min([44, 32, 86, 19])) #➞ 67
# Smallest number is 19, biggest is 86.
