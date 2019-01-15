# Create a function to multiply all values in a list by the amount of items
# contained in that list.

def MultiplyByLength(arr):
    count = 0
    for x in range(len(arr), -1):
        count += x
    for x in arr:
        total = x * count
    return total


print(MultiplyByLength([2, 3, 1, 0])) # [8, 12, 4, 0]
