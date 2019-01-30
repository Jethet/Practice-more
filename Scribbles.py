def letter_check(lst):
    lst1 = lst[0]
    lst2 = lst[1]
    lst1 = lst1.lower()
    lst2 = lst2.lower()
    for char in lst2:
        if char not in lst1:
            return False
    else:
        return True



print(letter_check(["trances", "nectar"])) # True
print(letter_check(["compadres", "DRAPES"])) # True
print(letter_check(["parses", "parsecs"])) # False
