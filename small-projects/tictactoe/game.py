from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None  # keep track of winner

    @staticmethod
    def make_board():
        return [" " for _ in range(9)]  # a single list to represent 3 x 3 board

    def print_board(self):
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        # tells us what number corresponds to what box on the board: 0 | 1 | 3 etc.
        number_board = [
            [str(i + 1) for i in range(j * 3, (j + 1) * 3)] for j in range(3)
        ]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def make_move(self, square, letter):
        # if valid move, make move: assign square to letter and return true
        # if invalid, return false
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if 3 in a row anywhere ... check everywhere
        # first, check row index (0, 1, or 2) by dividing every square and rounding down
        row_index = square // 3
        row = self.board[row_index * 3 : (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_index = square % 3
        column = [self.board[col_index + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonal spaces: these are the even index numbers 0, 2, 4, 6, 8
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all these checks fail, there is no winner
        return False

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def available_moves(self):
        # moves is empty list to be filled with spots that are still open:
        # for 'x' on row 1 spot 1 the list index is [(0, 'x')], etc.
        return [i for i, spot in enumerate(self.board) if spot == " "]
        # this is LIST COMPREHENSION of the below for loop:
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot == '':
        #         moves.append(i)
        # return moves


def play(game, x_player, o_player, print_game=True):

    # returns winner or None in case of tie
    if print_game:
        game.print_board_nums()

    letter = "X"  # starting letter
    # iterate while the game still has empty squares
    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + " makes a move to square {}".format(square + 1))
                game.print_board()
                print("")  # print empty line under printed board just for visual effect

            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter

            letter = "O" if letter == "X" else "X"

    if game.empty_squares():
        print(game.empty_squares())
        print("It's a tie!")


if __name__ == "__main__":
    x_player = HumanPlayer("X")
    o_player = RandomComputerPlayer("O")
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
