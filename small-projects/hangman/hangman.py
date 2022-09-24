import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)  #randomly chooses something from the list of words
    while '-' in word or '' in word:  # we do not want a dash or a space in a word
         word = random.choice(words)  # keep iterating to find a word without dash/space
    return word.upper() # uppercase all letters for this game

def hangman():
    word = get_valid_word(words)
    
    # keep track of letters that have already been guessed in a set (there can be no duplicates in a set)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()    # what the user has guessed

    user_letter = input("Guess a letter: ").upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print("You have already used that letter. Please choose again.")

    else:
        print("Invalid letter. Please choose again.")

user_input = input("Type a letter: ")
