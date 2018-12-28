# Given an array of ints, return the sum of the first 2 elements.
# If the array is less than 2, sum up the elements that exist,
# returning 0 if the array is length 0.

def sum2(nums):
    if len(nums) >= 2:
        return sum(nums[0:2])
    if len(nums) < 2:
        return sum(nums)


print(sum2([1, 2, 3]))
print(sum2([1, 1]))
print(sum2([1,1,1,1]))
