# Given a range of numbers, iterate from 0-th to end number and
# print the sum of the current number and previous numbers

def range_sum(nums):
    sum_old = 0
    for i in range(nums):
        sum = sum_old + i
        print(sum)
        sum_old = i


print(range_sum(10))
