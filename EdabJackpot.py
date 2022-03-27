# Create a function that takes a list (slot machine outcome) and returns True
# if all elements in the list are identical, and False otherwise.
# The list will contain 4 elements.
# The elements must be exactly identical for there to be a jackpot.

def test_jackpot(result):
        return len(set(result)) == 1


print(test_jackpot(["@", "@", "@", "@"])) #➞ True
print(test_jackpot(["abc", "abc", "abc", "abc"])) #➞ True
print(test_jackpot(["SS", "SS", "SS", "SS"])) #➞ True
print(test_jackpot(["&&", "&", "&&&", "&&&&"])) #➞ False
print(test_jackpot(["SS", "SS", "SS", "Ss"])) #➞ False
