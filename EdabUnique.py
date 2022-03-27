# Given a list of numbers, write a function that returns a list that:
# a)    Has all duplicate elements removed.
# b)    Is sorted from least to greatest value.

def unique_sort(lst):
    new_lst = []
    for x in lst:
        if x not in new_lst:
            new_lst.append(x)
    return sorted(new_lst)



print(unique_sort([1, 2, 4, 3])) # [1, 2, 3, 4]

print(unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2])) # [1, 2, 3, 4]

print(unique_sort([6, 7, 3, 2, 1])) # [1, 2, 3, 6, 7]
