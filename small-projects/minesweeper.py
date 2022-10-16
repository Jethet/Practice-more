import random
import re

# this game uses recursion and classes; it is a simple terminal version without UI
# create a board object to represent the game, so that the user can command
# "create a new board object", "dig here", or "render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        #keep track of parameters:
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # create board with helper function, plant bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()
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

    def assign_values_to_board(self):
        # when bombs are planted, a number from 0 to 8 is assigned for all empty spaces;
        # this represents how many neighbouring bombs there are
        for r in range(self.dim_size):
            for c in range (self.dim_size):
                if self.board[r][c] == '*':
                    continue    # if it is a bomb, we don't calculate anything
                self.board[r][c] = self.get_num_neighbor_bombs(r, c)
                
    def get_num_neighbor_bombs(self, row, col):
        # iterate through each of the neigbor positions and sum number of bombs;
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)

        num_neighbor_bombs = 0
        # min/max is used to make sure not to go out of bounds
        for r in range(max(0, row-1), min(self.dim_size-1, row+1) +1):
            for c in range(max(0, col-1), min(self.dim_size - 1, col+1) +1):
                if r == row and c == col:  # this is our original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighbor_bombs += 1
                    
        return num_neighbor_bombs                    

    def dig(self, row, col):
        # dig at given location, True if successful and False if bomb
        # possibilities are:
        # hit a bomb -> game over
        # dig location with neigboring bombs -> finish dig
        # dig at location without neighbor bombs -> recursively dig neighbors

        self.dug.add((row, col))    # keep track of places we have dug
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        # self.board[row][col] == 0 -> means not a bomb so check neighbors
        for r in range(max(0, row-1), min(self.dim_size-1, row+1) +1):
            for c in range(max(0, col-1), min(self.dim_size - 1, col+1) +1):
                if (r, c) in self.dug:
                    continue    # means: don't dig where you have already dug
                self.dig(r, c)

        # if our initial dig didn't hit a bomb, there should not be a bomb here
        return True
        
    def __str__(self):
        # magic function: prints out what this function returns
        # 1 - create a new array that represents what the user will see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range (self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # put this board representation in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                    )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-' * str_len + '\n' + string_rep + '-'*str_len

        return string_rep

# play the game
def play(dim_size=10, num_bombs=10):
    # 1 - create the board and plant the bombs
    board = Board(dim_size, num_bombs)
    
    # 2 - show the board,ask user where they want to dig
    # 3 - if location is a bomb, show 'game over' message
    
    # 4 - if loation is NOT a bomb, dig recursively until each square is at least
        # next to a bomb
    safe = True   #starting point, we have not dug anything
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        # re.split means anything the user writes from the regex (between '') is used
        # to split the two numbers: '0,0' or '0, 0' or even '0,   0'
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row, column: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue
        # if location is valid, we dig and assign returned value (True or False) to safe variable
        safe = board.dig(row, col)
        if not safe:
            # we dug a bomb, stop while loop
            break

    # 5 - repeat steps 2 to 4 until there are no more places to dig - you win,
    #     unless you dig a bomb - you lose
    if safe:
        print("Congratulations, you won!")
    else:
        print("Game over, this is a bomb!")

        #reveal the entire board:
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__':  # good practice: you are only running the file with this name
    play()