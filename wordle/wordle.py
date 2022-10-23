import random
# from colorama import init, Fore, Back
from words import wordList

# colorama.init()

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


    
