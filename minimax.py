import math

EMPTY = 0
HUMAN_PLAYER = 1
AI_PLAYER = 2

class Minimax():

    def __init__(self, depth):
        self.depth = depth

    def find_move(self, board):
        move = self.minimax(board, self.depth, True)[0]
        return move

    def get_heuristic(self, board):
        heuristic = 0

        for row in board.board:
            for j in range(board.columns - 3):
                lst = row[j:j+4]
                heuristic += self.evaluate_streak(lst)

        for j in range(board.columns):
            column = [row[j] for row in board.board]
            for i in range(board.rows - 3):
                lst = column[i:i+4]
                heuristic += self.evaluate_streak(lst)

        for i in range(board.rows - 3):
            for j in range(board.columns - 3):
                lst = [board.get_piece(i + k, j + k) for k in range(4)]
                heuristic += self.evaluate_streak(lst)

        for i in range(board.rows - 3):
            for j in range(board.columns - 3):
                lst = [board.get_piece(i + 3 - k, j + k) for k in range(4)]
                heuristic += self.evaluate_streak(lst)

        return heuristic

    def evaluate_streak(self, streak):
        heuristic = 0

        if streak.count(AI_PLAYER) == 4:
            heuristic += 1000
        elif streak.count(AI_PLAYER) == 3 and streak.count(EMPTY) == 1:
            heuristic += 50
        elif streak.count(AI_PLAYER) == streak.count(EMPTY) == 2:
            heuristic += 10
        elif streak.count(HUMAN_PLAYER) == streak.count(EMPTY) == 2:
            heuristic -= 10
        elif streak.count(HUMAN_PLAYER) == 3 and streak.count(EMPTY) == 1:
            heuristic -= 50
        elif streak.count(HUMAN_PLAYER) == 4:
            heuristic -= 1000

        return heuristic

    def minimax(self, board, depth, maximizing):
        if board.won_game(AI_PLAYER):
            return (-1, math.inf)
        if board.won_game(HUMAN_PLAYER):
            return (-1, -math.inf)
        if board.is_full():
            return (-1, 0)
        if depth == 0:
            return (-1, self.get_heuristic(board))

        if maximizing:
            valid_columns = board.get_valid_columns()
            best_move = valid_columns[len(valid_columns) // 2]
            best_score = -math.inf
            for move, child in board.get_children(AI_PLAYER):
                score = self.minimax(child, depth - 1, False)[1]
                if score > best_score:
                    best_score = score
                    best_move = move
        else:
            best_move = -1
            best_score = math.inf
            for move, child in board.get_children(HUMAN_PLAYER):
                score = self.minimax(child, depth - 1, True)[1]
                if score < best_score:
                    best_score = score
                    best_move = move

        return best_move, best_score
