# Create a function that takes two arguments (item, times).
# The first argument (item) is the item that needs repeating while
# the second argument (times) is the number of times the item is to be repeated.
# Return the result in a list.

def repeat(item, times):
    return [item] * times


print(repeat("edabit", 3)) # ["edabit", "edabit", "edabit"]
print(repeat(13, 5))   # [13, 13, 13, 13, 13]
print(repeat("7", 2))   # ["7", "7"]
print(repeat(0, 0))       # []
