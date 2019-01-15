# Create a function to multiply all values in a list by the amount of items
# contained in that list.

def MultiplyByLength(arr):
    count = len(arr)
    my_list = []
    for x in arr:
        x = x * count
        my_list.append(x)
    return my_list


print(MultiplyByLength([2, 3, 1, 0])) # [8, 12, 4, 0]
