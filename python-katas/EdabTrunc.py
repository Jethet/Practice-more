# Create a one line function that takes three arguments (txt, txt_length,
# txt_suffix) and returns a truncated string.
#    txt: Original string.
#    txt_length: Truncated length limit.
#    txt_suffix: Optional suffix string parameter.

# Truncated returned string length should adjust to passed length in parameters
# regardless of length of the suffix.

def truncate(txt, txt_length, *txt_suffix):
    return txt[0:txt_length]+str(txt_suffix).strip('()').replace("'", "").replace(",","")




print(truncate("CatDogDuck", 6, "Rat")) # "CatDogRat"
print(truncate("DogCat", 3)) # "Dog"
print(truncate("The quick brown fox jumped over the lazy dog.", 15, "...")) # "The quick br..."
