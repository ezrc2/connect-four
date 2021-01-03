import copy

EMPTY = 0

class Board():

    def __init__(self, piece, rows, columns):
        self.board = [[piece for j in range(columns)] for i in range(rows)]
        self.rows = rows
        self.columns = columns

    def drop_piece(self, column, piece):
        for i in range(self.rows - 1, -1, -1):
            if self.board[i][column] == EMPTY:
                self.board[i][column] = piece
                break

    def get_valid_columns(self):
        valid_columns = []
        for j in range(self.columns):
            column = [row[j] for row in self.board]
            if EMPTY in column:
                valid_columns.append(j)
        return valid_columns

    def get_children(self, piece):
        children = []
        for column in self.get_valid_columns():
            child = copy.deepcopy(self)
            child.drop_piece(column, piece)
            children.append((column, child))
        return children

    def is_full(self):
        for row in self.board:
            if EMPTY in row:
                return False
        return True

    def get_piece(self, row, col):
        return self.board[row][col]

    def won_game(self, piece):
        # check rows
        for row in range(self.rows):
            for col in range(self.columns - 3):
                if self.board[row][col] == piece and self.board[row][col + 1] == piece and \
                    self.board[row][col + 2] == piece and self.board[row][col + 3] == piece:
                    return True

        # check columns
        for row in range(self.rows - 3):
            for col in range(self.columns):
                if self.board[row][col] == piece and self.board[row + 1][col] == piece and \
                    self.board[row + 2][col] == piece and self.board[row + 3][col] == piece:
                    return True

        # check right diaganols
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                if self.board[row][col] == piece and self.board[row + 1][col + 1] == piece \
                    and self.board[row + 2][col + 2] == piece and \
                    self.board[row + 3][col + 3] == piece:
                    return True

        # check left diaganols
        for row in range(3, self.rows):
            for col in range(self.columns - 3):
                if self.board[row][col] == piece and self.board[row - 1][col + 1] == piece and \
                    self.board[row - 2][col + 2] == piece and \
                    self.board[row - 3][col + 3] == piece:
                    return True

        return False
