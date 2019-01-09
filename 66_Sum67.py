# Return the sum of the numbers in the array, except ignore sections of numbers
# starting with a 6 and extending to the next 7 (every 6 will be followed by at
# least one 7). Return 0 for no numbers.

def sum67(nums):
    sum = 0
    add = True
    for i in nums:
        while add == True:
            if i != 6:
                sum += i
                break
            else:
                add = False
        while add == False:
            if i != 7:
                break
            else:
                add = True

    return sum




print(sum67([1, 2, 2]))               #5
print(sum67([1, 2, 2, 6, 99, 99, 7])) #5
print(sum67([1, 1, 6, 7, 2]))         #4
