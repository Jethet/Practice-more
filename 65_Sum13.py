# Return the sum of the numbers in the array, returning 0 for an empty array.
# Except the number 13 is very unlucky, so it does not count and numbers that
# come immediately after a 13 also do not count.

def sum13(nums):
    sum = 0
    for i in range(0, len(nums), 1):
        if nums[i] != 13 and nums[i -1] != 13:
            sum += nums[i]
        return sum


    """
    if 13 in nums:
        x = nums.index(13)
        return sum(nums[:x]) + sum(nums[x+2:])
    elif nums == '':
        return 0
    else:
        return sum(nums)
        """


print(sum13([1, 2, 2, 1])) # 6
print(sum13([1, 1])) # 2
print(sum13([1, 2, 2, 1, 13])) # 6
