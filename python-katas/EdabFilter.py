# Create a function that takes a list of non-negative numbers and strings
# and return a new list without the strings. Zero is a non-negative number.

def filter_list(lst):
    return [x for x in lst if isinstance(x, int)]


"""
def filter_list(lst):
    new_list = []
    for x in lst:
        if isinstance(x, int) == True:
            new_list.append(x)

    return new_list
"""


print(filter_list([1, 2, "a", "b"])) # [1, 2]
print(filter_list([1, "a", "b", 0, 15])) # [1, 0, 15]
print(filter_list([1, 2, "aasf", "1", "123", 123])) # [1, 2, 123]
