# Find the total number of digits a given number has
def find_digit_amount(num):
	return len(str(num))

print(find_digit_amount(15))   # = 2

# Create a function that takes a list and a string as arguments
# and return the index of the string.
def find_index(lst, txt):
	return lst.index(txt)

print(find_index(['abc', 'cde', 'efg'], 'cde'))   # = 1

# Create a function that takes a string and returns the word count.
# The string will be a sentence.
def count_words(txt):
	return len(txt.split())

print(count_words('Did you see that coming?'))   # = 5
