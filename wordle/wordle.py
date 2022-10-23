import random
from words import wordList


blue = '\033[94m' 
red = '\033[91m' 
green = '\033[92m'

def randomWord():
    randWord = random.choice(wordList)
    return randWord

def game(randWord):
    guess = input("Please enter your word: ")
    guessNumber = 0

    for x in guess:
        if x in randWord:
            print(x)

    print(randWord)

    guessNumber += 1
    # print(guessNumber)
            

game(randomWord())


    
