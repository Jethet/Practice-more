# Accept two int values from user and return their product.
# If the product is greater than 1000, then return their sum

def mult_num(value1, value2):
    sum_mult = value1 * value2
    if sum_mult <= 1000:
        return sum_mult
    if sum_mult > 1000:
        return value1 + value2

value1 = int(input("Please enter the first integer. "))
value2 = int(input("Please enter the second integer. "))

print(mult_num(value1, value2))
