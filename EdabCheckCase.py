# Create a function that returns True if an input string contains only uppercase
# or only lowercase letters.

def same_case(txt):
    return txt.islower() or txt.isupper()


print(same_case("hello")) #➞ True
print(same_case("HELLO")) #➞ True
print(same_case("Hello")) #➞ False
print(same_case("ketcHUp")) #➞ False
