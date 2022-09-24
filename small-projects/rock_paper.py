import random

# Game rules: rock beats scissors, scissors beat paper, paper beats rock

def play():
    user = input("'R' for Rock, 'P' for Paper, 'S' for scissors")
    computer = random.choice(['R', 'P', 'S'])

    if user == computer:
        return 'Tie!'

def is_winner(player, computer):
    # returns 'true' if player wins
    