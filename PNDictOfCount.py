# Given a list, iterate it and count the occurrence of each element and create
# a dictionary to show the count of each element.
# Expected Outcome: dict = {10: 2, 20: 2, 30: 1, 40: 1, 50: 1}

list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
mydict = {}
for x in list:
    number = list.count(x)
    mydict.update({x : number})
print(mydict)
