# Create a function that takes a list of numbers and returns the sum of the two
# lowest positive numbers. Don't count negative numbers.

def sum_two_smallest_nums(lst):
    new_lst = [x for x in lst if x >= 0]
    return sum((sorted(new_lst))[0:2])


print(sum_two_smallest_nums([19, 5, 42, 2, 77])) # 7
print(sum_two_smallest_nums([10, 343445353, 3453445, 3453545353453])) # 3453455
print(sum_two_smallest_nums([2, 9, 6, -1])) # 8
print(sum_two_smallest_nums([879, 953, 694, -847, 342, 221, -91, -723, 791, -587])) # 563
print(sum_two_smallest_nums([3683, 2902, 3951, -475, 1617, -2385])) # 4519
