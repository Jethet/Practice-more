nums = [1, 2, 2, 1, 13, 4, 5]
x = nums.index(13)
y = sum(nums[:x])
z = sum(nums[x+2:])
print(y, z)
