# Create a function that accepts a string of space separated integers and returns
# the highest and lowest integers (as a string).
# Output string must be two integers separated by a single space, and highest
# number is first.

def high_low(txt):
	numbers = [int(num) for num in txt]
	#a = max(numbers)
	#b = min(numbers)
	return str(numbers)


print(high_low("1 2 3 4 5")) # "5 1"
print(high_low("1 2 -3 4 5")) # "5 -3"
print(high_low("1 9 3 4 -5")) # "9 -5"
print(high_low("13")) # "13 13"
