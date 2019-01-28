# Create a function that takes a string and returns the number of alphanumeric
# characters that occur more than once. The input string can be assumed to
# contain only alphanumeric characters (digits + uppercase and lowercase letters).

def duplicate_count(txt):
    lst = []
    for x in txt:
        if txt.count(x) > 1 and x not in lst:
            lst.append(x)
    return len(lst)



print(duplicate_count("abcde")) # 0

print(duplicate_count("aabbcde")) # 2

print(duplicate_count("Indivisibilities")) # 2
