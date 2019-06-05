# Write a function that returns True if a dictionary is empty and False otherwise.

def is_empty(dictionary):
    if dictionary == {}:
        return True
    else:
        return False

print(is_empty({})) #➞ True
print(is_empty({ "a": 1 })) #➞ False
