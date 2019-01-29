def sum_neg(lst):
	if lst:
		countPos = len([i for i in lst if i > 0])
		sumNeg = sum([i for i in lst if i < 0])
		return [countPos, sumNeg]
	else:
		return lst

print(sum_neg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])) # [10, -65]

print(sum_neg([92, 6, 73, -77, 81, -90, 99, 8, -85, 34])) # [7, -252]

print(sum_neg([91, -4, 80, -73, -28])) # [2, -105]

print(sum_neg([])) # []
