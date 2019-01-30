def letter_check(lst):
    lst1 = lst[0]
    lst2 = lst[1]
    lst1 = lst1.lower()
    lst2 = lst2.lower()
    if lst2 in lst1:
            return True




print(letter_check(["trances", "nectar"])) # True

print(letter_check(["compadres", "DRAPES"])) # True

print(letter_check(["parses", "parsecs"])) # False
