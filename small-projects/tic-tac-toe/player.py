import math
import random

class Player:
    def __init__(self, letter):
        # letter is X or O
        self.letter = letter

    # every player gets a next move
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass