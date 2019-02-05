# Given two sets, check if one set is subset or superset of another set.
# If the subset is found delete all elements from that set.

firstSet  = {57, 83, 29}
secondSet = {57, 83, 29, 67, 73, 43, 48}

if firstSet <= secondSet:
    firstSet.clear()
if firstSet>= secondSet:
    secondSet.clear()

print(firstSet, secondSet)
