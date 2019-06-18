# Create a function that checks if the argument is an integer or a string.
# If it's an integer, return "int", if it's a string, return "str".

def int_or_string(var):
    if type(var) == str:
        return "str"
    if type(var) == int:
        return "int"


print(int_or_string(3)) #➞ "int"
print(int_or_string("Hello")) #➞ "str"
print(int_or_string(8)) #➞ "int"
print(int_or_string("Yo")) #➞ "str"
print(int_or_string(9843532)) #➞ "int"
