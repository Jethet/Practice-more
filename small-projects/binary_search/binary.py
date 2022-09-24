# binary search: divide list by finding middle element
# is target element bigger (to the right) or smaller (to the left) of middle element
# for example smaller: then divide left part of list to find middle element, and again check:
#   => is target element bigger (to the right) or smaller (to the left) of middle element

def binary_search(list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(list) - 1

    if high < low:
        return -1
    
    midpoint = (low + high) // 2
    
    if target == midpoint:
        return target
    elif target < midpoint:
        return binary_search(list, target, low, midpoint-1)
    else:
        return binary_search(list, target, midpoint+1, high)

if __name__ == "__main__":
    list = range(99)
    target = 25
    print(binary_search(list, target))
