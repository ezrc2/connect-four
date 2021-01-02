EMPTY = 0

class Board():

    def __init__(self, player, rows, columns):
        self.board = [[player for j in range(columns)] for i in range(rows)]
        self.rows = rows
        self.columns = columns

    def drop_piece(self, column, player):
        for i in range(self.rows - 1, -1, -1):
            if self.board[i][column] == EMPTY:
                self.board[i][column] = player
                break

    def is_board_full(self):
        for row in self.board:
            for value in row:
                if value == EMPTY:
                    return False
        return True

    def won_game(self, player):
        # check rows
        for row in range(self.rows):
            for col in range(self.columns - 3):
                if self.board[row][col] == player and self.board[row][col + 1] == player and \
                    self.board[row][col + 2] == player and self.board[row][col + 3] == player:
                    return True

        # check columns
        for row in range(self.rows - 3):
            for col in range(self.columns):
                if self.board[row][col] == player and self.board[row + 1][col] == player and \
                    self.board[row + 2][col] == player and self.board[row + 3][col] == player:
                    return True

        # check right diaganols
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                if self.board[row][col] == player and self.board[row + 1][col + 1] == player \
                    and self.board[row + 2][col + 2] == player and \
                    self.board[row + 3][col + 3] == player:
                    return True

        # check left diaganols
        for row in range(3, self.rows):
            for col in range(self.columns - 3):
                if self.board[row][col] == player and self.board[row - 1][col + 1] == player and \
                    self.board[row - 2][col + 2] == player and \
                    self.board[row - 3][col + 3] == player:
                    return True

        return False