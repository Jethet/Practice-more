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

# x = tuple([x**2 for x in range(10)])
# print(x)

# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)# show that duplicates have been removed
# print('orange' in basket)
# print('juice' in basket)

# x = ['apple', 'orange', 'apple', 'banana', 'peach']
# print(x)
# print(set(x))

# a = set('abracadabra')
# b = set('alacazam')
# print(a)     # unique letters in a
# print(a - b) # letters in a but not in b
# print(a | b) # letters in a or b or both
# print(a & b) # letters in both a and b
# print(a ^ b) # letters in a or b but not both

# myDict = { 'a': 1, 'b': 2, 'c': 3}
# print(myDict)
# newDict = {1: [1,2,3], 'a': {1: 'a', 2: 'b'}}
# print(newDict)

# print(newDict['a'])

# myDict = {'a': 1, 'b': 2, 'c': 3}
# myDict['f'] = 'new value'
# print(myDict)
# print(len(myDict))

# myKeys = 22, 33, 44
# myValues = 0
# newDict = dict.fromkeys(myKeys, myValues)
# print(newDict)
# x = {x: x**2 for x in (2, 3, 4)}
# print(x)

# a = dict(a=1, b=2, c=3)
# print(a)

# if 3 > 2:
#   print('Yes')
# else:
#   print('No')

def http_error(status):
  match status:
    case 400:
      return "bad request"
    case 404:
      return "not found"
    case 418:
      return "no idea"
    case _:
      return "something is wrong"
    
print(http_error(502))