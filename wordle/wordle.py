import random
from words import wordList

def randomWord():
    randWord = random.choice(wordList)
    return randWord

def game(randWord):
    guess = input("Please enter your word: ")

    for x in guess:
        if x in randWord:
            print(x)

    print(randWord)
            

game(randomWord())


    
