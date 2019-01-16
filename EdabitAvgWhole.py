# Create a function that takes a list as an argument and returns True or False
# depending on if the average of all elements in the list is a whole number or not.

def is_avg_whole(arr):
    average = sum(arr) / len(arr)
    if average % 2 == 0:
        return True
    else:
        return False




print(is_avg_whole([1, 3]))     # True
print(is_avg_whole([1, 2, 3, 4])) # False
print(is_avg_whole([1, 5, 6]))   # True
print(is_avg_whole([1, 1, 1]))   # True
print(is_avg_whole([9, 2, 2, 5]))  # False
