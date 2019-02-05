# Given a list slice it into three equal chunks and reverse each list.
# Expected Outcome:   FirstList = [3, 2, 1]
#                     SecondList = [6, 5, 4]
#                     ThirdList = [9, 8, 7]

sampleList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
FirstList = sampleList[0:3]
SecondList = sampleList[3:6]
ThirdList = sampleList[6:]
print(FirstList[::-1], SecondList[::-1], ThirdList[::-1])
