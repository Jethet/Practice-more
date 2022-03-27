# Create a function that takes the month and year (as integers) and returns
# the number of days in that month.

def day_amount(month, year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) or (year == 1000):
        if month == 2:
            return 29
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    else:
        return 28

print(day_amount(2, 2018)) # 28
print(day_amount(3, 2011)) # 31
print(day_amount(4, 654)) # 30
print(day_amount(2, 2020)) # 29
print(day_amount(2, 200)) # 28
print(day_amount(2, 1000)) # 29
