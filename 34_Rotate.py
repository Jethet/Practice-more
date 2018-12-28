# Given an array of ints length 3, return an array with the elements
# 'rotated left', i.e. first element moves to the end of the array.

def rotate_left3(nums):
        return nums[1:] + [nums[0]]

print(rotate_left3([1, 2, 3]))
print(rotate_left3([5, 11, 9]))
print(rotate_left3([7, 0, 0]))
