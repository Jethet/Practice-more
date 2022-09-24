import random

# instead of the computer generating a random number, the user is giving the number

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        # you cannot have low and high be the same:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high because low and high are the same here
            
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?".lower())
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"The computer guessed your number, {guess} correctly!")

computer_guess(10)