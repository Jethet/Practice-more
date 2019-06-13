# Create a function that counts the number of syllables a word has.
# Each syllable is separated with a dash -.

def number_syllables(word):
    return word.count("-") + 1

print(number_syllables("buf-fet")) #➞ 2
print(number_syllables("beau-ti-ful")) #➞ 3
print(number_syllables("mon-u-men-tal")) #➞ 4
print(number_syllables("on-o-mat-o-poe-ia")) #➞ 6
