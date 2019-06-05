# You've got chickens (2 legs), cows (4 legs) and pigs (4 legs) on your farm.
# Return the total number of legs on your farm.

def animals(chickens, cows, pigs):
    return (chickens*2) + (cows*4) + (pigs*4)

print(animals(2, 3, 5)) #➞ 36
print(animals(1, 2, 3)) #➞ 22
print(animals(5, 2, 8)) #➞ 50
