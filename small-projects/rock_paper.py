import random

# Game rules: rock beats scissors, scissors beat paper, paper beats rock


def play():
    user = input("What's your choice? 'R' for Rock, 'P' for Paper, 'S' for scissors\n")
    computer = random.choice(["R", "P", "S"])

    if user == computer:
        return "It's a tie!"

    if is_winner(user, computer):
        return "You won!"

    return "You lost!"


def is_winner(player, opponent):
    # returns 'true' if player wins
    if (
        (player == "R" and opponent == "S")
        or (player == "S" and opponent == "P")
        or (player == "P" and opponent == "R")
    ):
        return True


print(play())
