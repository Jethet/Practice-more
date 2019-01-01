# Two strings: return True if either string appears at the end of the other
# string (not case sensitive). s.lower() returns lowercase version of string.

def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if a.endswith(b) or b.endswith(a):
        return True
    else:
        return False

#CodingBat solution:
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return (b.endswith(a) or a.endswith(b))

print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))
