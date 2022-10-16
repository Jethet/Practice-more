# Given an array of 3 ints, find out if first or last element is larger and then
# set all elements to be that value. Return the changed array.

def max_end(nums):
    if nums[2] > nums[0]:
        nums[0] = nums[2]
        nums[1] = nums[2]
        return nums
    elif nums[2] < nums[0]:
        nums[1] = nums[0]
        nums[2] = nums[0]
        return nums
    elif nums[0] == nums[2]:
        nums[1] = nums[0]
        return nums

# ALTERNATIVE:
def max_end(nums):
    big = max(nums[0], nums[2])
    nums[0] = big
    nums[1] = big
    nums[2] = big
    return nums


print(max_end([11, 5, 9]))
print(max_end([1, 2, 3]))
print(max_end([2, 2, 2]))
