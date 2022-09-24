import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list of words
    while "-" in word or " " in word:  # we do not want a dash or a space in a word
        word = random.choice(words)  # keep iterating to find a word without dash/space

    return word.upper()  # uppercase all letters for this game


def hangman():
    word = get_valid_word(words)
    # keep track of letters that have already been guessed in a set (there can be no duplicates in a set)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    # user can keep guessing until all word letters have been removed from the set as long as they have lives
    while len(word_letters) > 0 and lives > 0:  
        # let user know which letters they have used already
        print("You have ", lives, " left and you have used these letters: ", " ".join(used_letters))

        # what the word is with dashes where they have not guessed, i.e. E X A - M P L E
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("The current word is: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("")
            else:
                lives = lives - 1
                print("\nYour letter, ", user_letter, " is not in the word.")

        elif user_letter in used_letters:
            print("\nYou have already used that letter. Please choose again.")

        else:
            print("\nInvalid letter. Please choose again.")
            
    if lives == 0:
        print("Sorry, you died. The word was ", word)
    else:
        print("You guessed the word ", word, " !!")

hangman()