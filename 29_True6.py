# Given an array of ints, return True if 6 appears as either the first
# or the last element in the array.

def first_last6(nums):
    if nums[0] or nums[-1] == 6:
        return True

print(first_last6([1, 2, 6]))
print(first_last6([6, 1, 2, 3]))
print(first_last6([13, 6, 2, 3]))
