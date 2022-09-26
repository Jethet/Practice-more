
class TicTacToe:
    def __init__(self, board):
        self.board = ['' for _ in range(9)]  # a single list to represent 3 x 3 board
        self.current_winner = None           # keep track of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # tells us what number corresponds to what box on the board: 0 | 1 | 3 etc.
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # moves is empty list to be filled with spots that are still open:
        # for 'x' on row 1 spot 1 the list index is [(0, 'x')], etc.
        return [i for i, spot in enumerate(self.board) if spot == '']
        # this is LIST COMPREHENSION of the below for loop:
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot == '':
        #         moves.append(i)
        # return moves