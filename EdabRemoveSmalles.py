# Create a function that takes a list of integers and removes the smallest value.
# Don't change the order of the left over items.
# If you get an empty list, return an empty list: [] ➞ [].
# If there are multiple items with the same value, remove item with lower index
# (3rd example).

def remove_smallest(lst):
    if lst == []:
        return list('')
    lst.remove(min(lst))
    return lst



print(remove_smallest([1, 2, 3, 4, 5])) # [2, 3, 4, 5]

print(remove_smallest([5, 3, 2, 1, 4])) # [5, 3, 2, 4]

print(remove_smallest([2, 2, 1, 2, 1])) # [2, 2, 2, 1]
