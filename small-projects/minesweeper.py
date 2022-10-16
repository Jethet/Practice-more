# this game uses recursion and classes; it is a simple terminal version without UI

import random

# create a board object to represent the game, so that the user can command
# "create a new board object", "dig here", or "render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        #keep track of parameters:
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # create board with helper function, plant bombs
        self.board = self.make_new_board
        # use a set to keep track of used locations; save (row, col) tuples in the set
        self.dug = set()    # if we dig at location 0, 0, then self.dug = {(0,0)}

    def make_new_board(self):
        # we use a list of lists here for a two-dimensional board; 
        # each sublist is a row of the board
        # generate a new board: [[None, None, ..., None],[None, ..., None], [ ....]] to
        # represent a board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            location = random.randint(0, self.dim_size ** 2 - 1)
            row = location // self.dim_size   # number of times dim_size goes into location
            col = location % self.dim_size    # remainder indicates index in row to look for

            if board[row][col] == '*':    # if == '*', there is a bomb in that location, so continue
                continue

            board[row][col] = '*'   # plant a bomb
            bombs_planted += 1

        return board
                
        
    

# play the game
def play(dim_size=10, num_bombs=10):
    # 1 - create the board and plant the bombs
    # 2 - show the board,ask user where they want to dig
    # 3 - if location is a bomb, show 'game over' message
    # 4 - if loation is NOT a bomb, dig recursively until each square is at least
        # next to a bomb
    # 5 - repeat steps 2 to 4 until there are no more places to dig - you have a winner
    pass