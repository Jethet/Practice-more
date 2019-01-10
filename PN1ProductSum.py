# Accept two int values from user and return their product.
# If the product is greater than 1000, then return their sum


value1 = int(input("Please enter the first integer. "))
value2 = int(input("Please enter the second integer. "))
if value1 * value2 <= 1000:
    print(value1*value2)
if value1 * value2 > 1000:
    print(value1 + value2)
