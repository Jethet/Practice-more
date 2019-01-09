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

# Create a function that takes a number (from 1 to 12) and return its
# corresponding month name as a string.
def month_name(num):
    months = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
     7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    return months.get(num)

print(month_name(4))
