# Party successful when the number of cigars is between 40 and 60, inclusive.
# Unless it is the weekend, when there is no upper bound on the number of cigars.
# Return True if the party with the given values is successful, or False otherwise.

def party(cigars, weekend):
    if cigars >= 40 and cigars <= 60:
        return True
    elif cigars >= 40 and weekend == True:
        return True
    else:
        return False

print(party(30, False))
print(party(50, False))
print(party(70, True))
