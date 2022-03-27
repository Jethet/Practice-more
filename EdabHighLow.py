# Create a function that accepts a string of space separated integers and returns
# the highest and lowest integers (as a string).
# Output string must be two integers separated by a single space, and highest
# number is first.

def high_low(txt):
	numbers = txt.split()
	a = max(numbers, key=int)
	b = min(numbers, key=int)
	return str(str(a) + ' '+  str(b))

print(high_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
print(high_low("1 2 3 4 5")) # "5 1"
print(high_low("1 2 -3 4 5")) # "5 -3"
print(high_low("1 9 3 4 -5")) # "9 -5"
print(high_low("13")) # "13 13"
