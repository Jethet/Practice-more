# Create a function that takes a list of numbers and returns the sum of its cubes.
# If given an empty list, return 0.

def sum_of_cubes(nums):
    return sum([(num**3) for num in nums])


print(sum_of_cubes([1, 5, 9])) #➞ 855
# Since 1^3 + 5^3 + 9^3 = 1 + 125 + 729 = 855
print(sum_of_cubes([3, 4, 5])) #➞ 216
print(sum_of_cubes([2])) #➞ 8
print(sum_of_cubes([])) #➞ 0
