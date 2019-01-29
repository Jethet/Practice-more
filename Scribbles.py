def day_amount(month, year):
	if month in (1,3,5,7,8,10,12):
		return 31
	elif month in (4,6,9,11):
		return 30
	else: # month == 2
		if any([year % 4 == 0 and not year % 100 == 0, year % 400 == 0 ]):
			return 29
		else:
			return 28

print(day_amount(2, 2018)) # 28
print(day_amount(3, 2011)) # 31
print(day_amount(4, 654)) # 30
print(day_amount(2, 2020)) # 29
print(day_amount(2, 200)) # 28
print(day_amount(2, 1000)) # 29
