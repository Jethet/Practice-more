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

# Create a function that counts how often txt1 appears in txt2
def char_count(txt1, txt2):
    count = txt2.count(txt1)
    return count

print(char_count('a', 'abcabc'))

# Create a function that takes a number (from 1 to 12) and return its
# corresponding month name as a string.
def month_name(num):
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', \
    6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', \
    11: 'November', 12: 'December'}
    return months.get(num)

print(month_name(11))
