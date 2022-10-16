# Create a function that takes any non-negative number as an argument and
# returns it with its digits in descending order. Descending order is when you
# sort from highest to lowest. Expect non-negative numbers for all test cases.

def sort_decending(num):
    num_lst = str(num)
    desc_num = sorted(num_lst, reverse = True)
    return int(''.join(desc_num))



print(sort_decending(123)) # 321

print(sort_decending(1254859723)) # 9875543221

print(sort_decending(73065)) # 76530
