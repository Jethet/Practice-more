import random

# generate random number
# randomNum = (random.randrange(0,10)) 
compNum = random.randrange(1, 20)

myNum = int(input("Please enter a number between 1 and 20: "))

if myNum == compNum:
  print("You have won!")
else:
  print("Try again")
