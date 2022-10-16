# Create a function that takes a string (will be a persons first and last name
# with one space in between), returns a string with first and last name swapped.

def name_shuffle(txt):
    txt = txt.split()
    new_text = txt[::-1]
    return ' '.join(new_text)

# one solution from Edabit:
def nameShuffle(str):
  first, last = str.split()
  return ' '.join([last, first])


print(name_shuffle("Donald Trump")) # "Trump Donald"
print(name_shuffle("Rosie O'Donnell")) # "O'Donnell Rosie"
print(name_shuffle("Seymour Butts")) # "Butts Seymour"
