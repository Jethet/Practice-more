my_nums = [1,2,3,4,5,6,7]
def double(value):
    return value % 2 == 0

print(list(filter(double, my_nums)))
