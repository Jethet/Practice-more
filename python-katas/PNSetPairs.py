# Given two lists of equal size create a set such that it shows the element
# from both lists in the pair.

firstList = [2, 3, 4, 5, 6, 7, 8]
secondList = [4, 9, 16, 25, 36, 49, 64]

# with zip() an iterator is created that aggregates the iterables that are
# passed; the result is an iterator of tuples must be assigned to a set:

newlist = zip(firstList,secondList)
paired_list = set(newlist)
print(paired_list)
