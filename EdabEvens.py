# Create a function that takes a list of numbers and returns only the even values.

def noOdds(lst):
    even = []
    for x in lst:
        if x % 2 == 0:
            even.append(x)
    return even


print(noOdds([1, 2, 3, 4, 5, 6, 7, 8])) # [2, 4, 6, 8]
print(noOdds([43, 65, 23, 89, 53, 9, 6])) # [6]
print(noOdds([718, 991, 449, 644, 380, 440])) # [718, 644, 380, 440]
