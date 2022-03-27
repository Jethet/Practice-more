# Create a function that takes a list of lists with integers or floats.
# Return a new (single) list with the largest numbers from each.
# Watch out for negative integers (numbers).

def findLargestNums(lst):
    return [max(i) for i in lst]
    
"""
    # with list comprehension:

     return list(map(max, lst))
"""

print(findLargestNums([[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]])) # [7, 90, 2]
print(findLargestNums([[-34, -54, -74], [-32, -2, -65], [-54, 7, -43]]))
# [-34, -2, 7]
print(findLargestNums([[0.4321, 0.7634, 0.652], [1.324, 9.32, 2.5423, 6.4314], [9, 3, 6, 3]]))
# [0.7634, 9.32, 9]
