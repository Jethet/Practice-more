# Given two lists, create a third list by picking an odd-index element from the
# first list and even index elements from second.
# Expected Outcome: [6, 12, 18, 4, 12, 20, 28]


listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

listThree = listOne[1:-1:2] + listTwo[0::2]
print(listThree)
