# Given an input list remove the element at index 4 and add it to the 2nd
# position and also, at the end of the list
# Expected Outcome: [54, 44, 79, 27, 91, 41, 79]

mylist = [54, 44, 27, 79, 91, 41]
val = mylist.pop(3)
newlist1 = mylist[0:2]
newlist1.append(val)
newlist2 = mylist[-3:]
newlist2.append(val)
newlist = newlist1 + newlist2
print(newlist)
