# Given string of 4 and a word, return a new string where the word is
# in the middle of the string of 4.

def make_out_word(out, word):
    return out[0:2] + word + out[2:]

print(make_out_word('<<>>','Yay'))
