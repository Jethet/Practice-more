import random

# generate random number
# randomNum = (random.randrange(0,10)) 

def guessingGame(x):
  compNum = random.randrange(1, x)
  guess = 0
  
  while guess != compNum:
    guess = int(input(f"Please enter a number between 1 and {x}: "))
  
    if guess < compNum:
      print("Your guess is too low")
    elif guess > compNum:
      print("Your guess is too high")
    elif guess == compNum:
      print("You have won!")

guessingGame(10)