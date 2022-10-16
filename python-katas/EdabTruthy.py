# In Python, a truthy value is a value that translates to True when evaluated in
# a Boolean context. All values are truthy unless they're defined as falsy.
# All falsy values are as follows:
#    False
#    None
#    0
#    []
#    {}
#    ""
# Create a function that takes an argument of any data type and returns 1 if it's
# truthy and 0 if it's falsy.

def is_truthy(val):
    datalist = [False, None, 0, [], {}, ""]
    if val not in datalist:
        return 1
    else:
        return 0


print(is_truthy(0)) #➞ 0
print(is_truthy(False)) #➞ 0
print(is_truthy("")) #➞ 0
print(is_truthy("False")) #➞ 1
