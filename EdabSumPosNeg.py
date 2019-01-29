# Create a function that takes a list of positive and negative numbers.
# Return a list where the first element is the count of positive numbers and
# the second element is the sum of negative numbers. If the input list is empty,
# return an empty list.

def sum_neg(lst):
    pos = []
    neg = []
    for x in lst:
        if x >= 0:
            pos.append(x)
        elif x < 0:
            neg.append(x)
    return [len(pos), sum(neg)]



print(sum_neg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])) # [10, -65]

print(sum_neg([92, 6, 73, -77, 81, -90, 99, 8, -85, 34])) # [7, -252]

print(sum_neg([91, -4, 80, -73, -28])) # [2, -105]

print(sum_neg([])) # []
