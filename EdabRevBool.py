# Create a function that reverses a boolean value and returns the string
# "boolean expected" if another variable type is given.

def reverse(arg):    # code is not correct
    if arg = bool:
        return not arg
    else:
        return "boolean expected"

# Examples Edabit:
def reverse(arg):
	if isinstance(arg, bool):
		return not arg
	else:
		return('boolean expected')

def reverse(arg=None):
	return not arg if type(arg) == bool else "boolean expected"

print(reverse(True)) # False
print(reverse(False)) # True
print(reverse(0)) # "boolean expected"
print(reverse(None)) # "boolean expected"
