# Create a function that returns the number of hashes and pluses in a string.

def hash_plus_count(txt):
    x = txt.count("#")
    y = txt.count("+")
    return [x, y]

print(hash_plus_count("###+")) #➞ [3, 1]
print(hash_plus_count("##+++#")) #➞ [3, 3]
print(hash_plus_count("#+++#+#++#")) #➞ [4, 6]
print(hash_plus_count("")) #➞ [0, 0]
