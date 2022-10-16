# Count the amount of ones in the binary representation of an integer.
# So for example, since 12 is '1100' in binary, the return value should be 2.

def count_ones(num):
    bin_rep = bin(num)
    count = 0
    for x in map(int, bin_rep[2:]):
        if x == 1:
            count +=1
    return count


print(count_ones(0))  # 0
print(count_ones(100)) # 3
print(count_ones(999)) # 8
