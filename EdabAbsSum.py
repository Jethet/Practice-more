# Take a list of integers (positive or negative or both) and return the sum of
# the absolute value of each element.


def get_abs_sum(lst):
    my_list = []
    for x in lst:
        x = abs(x)
        my_list.append(x)
    return sum(my_list)


print(get_abs_sum([2, -1, 4, 8, 10])) # 25
print(get_abs_sum([-3, -4, -10, -2, -3])) # 22
print(get_abs_sum([2, 4, 6, 8, 10])) # 30
print(get_abs_sum([-1])) # 1
