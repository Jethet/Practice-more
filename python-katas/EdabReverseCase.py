# Given a string, create a function to reverse the case. All lower-cased letters
# should be upper-cased, and vice versa.

def reverse_case(txt):
    return txt.swapcase()

print(reverse_case("Happy Birthday")) #➞ "hAPPY bIRTHDAY"
print(reverse_case("MANY THANKS")) #➞ "many thanks"
print(reverse_case("sPoNtAnEoUs")) #➞ "SpOnTaNeOuS"
