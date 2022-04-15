# x = 3
# y = 5
# print(x ** y)

# myList = [1,2,3,4,5,6,7,8]
# newList = ['a', 'b', 'c', 'd', 'e']
# numList = myList[:]
# numList[4] = 12
# myList[4] = 'x'
# myList.append(25)
# myList.append(7 + 12)
# print(len(myList))

# x = [[1, 2, 3], [4, 5, 6]]

# print(x[1][2])  

# y = []
# for x in range(10):
#   y.append(x*2)

# y = [x * 2 for x in range(10)]
# print(y)

# myTuple = (234, 567, 8910, 8910)
# print(myTuple[0])
# print(myTuple.count(567))
# print(myTuple.index(8910))
# newTuple = myTuple, (1,2,3,4)
# print(newTuple)
# anotherTuple = (newTuple, ['a', 'b', 'c'])
# anotherTuple[1][2] = 'd'
# print(anotherTuple)
# print(anotherTuple[-1][-1])

# x, y = anotherTuple
# print(x)
# print(y)

# myList = [1, 2, 3]
# x = tuple(myList)

x = tuple([x**2 for x in range(10)])
print(x)