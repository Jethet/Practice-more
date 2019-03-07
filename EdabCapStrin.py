# Create a function that takes a string as an argument and converts the first
# character of each word to uppercase. Return the newly formatted string.

def make_title(txt):
	return ' '.join(word[0].upper() + word[1:] for word in txt.split())

print(make_title("i aM a tITLE"))
print(make_title("This is a title")) # "This Is A Title"
print(make_title("capitalize every word")) # "Capitalize Every Word"
print(make_title("I Like Pizza")) # "I Like Pizza"
print(make_title("PIZZA PIZZA PIZZA")) # "PIZZA PIZZA PIZZA"
