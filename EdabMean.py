# Create a function that takes a list of numbers and returns the mean value.
# Round to two decimal places.

def mean(lst):
    x = len(lst)
    y = sum(lst)
    return round((y / x), 2)


print(mean([1, 0, 4, 5, 2, 4, 1, 2, 3, 3, 3])) # 2.54
print(mean([2, 3, 2, 3])) # 2.50
print(mean([3, 3, 3, 3, 3])) # 3.00
