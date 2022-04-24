import random

print("Guess a number between 1 and 10!")

# generate random number
randomNum = (random.randrange(1,10)) 

# input number
num = int(input("Please enter a number: "))

# compare number
if num > 10:
    print("You must enter a number between 1 and 10!")
elif num == randomNum:
  print("You guessed it!")
else:
  print("Too bad, try again")

# print outcome
# print("This is the secret number: ", randomNum)