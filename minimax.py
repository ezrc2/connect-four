import math

EMPTY = 0
HUMAN_PLAYER = 1
AI_PLAYER = 2

class Minimax():

    def __init__(self, depth):
        self.depth = depth

    def find_move(self, board):
        move, j = self.minimax(board, self.depth, True)
        print (move, j)
        return move

    def get_heuristic(self, board):
        heuristic = 0

        

        return heuristic


    def minimax(self, board, depth, maximizing):
        if depth == 0:
            return (-1, self.get_heuristic(board))
        if board.won_game(AI_PLAYER):
            return (-1, math.inf)
        if board.won_game(HUMAN_PLAYER):
            return (-1, -math.inf)
        if board.is_full():
            return (-1, 0)

        if maximizing:
            best_move = -1
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
                if score > best_score:
                    best_score = score
                    best_move = move

        return best_move, best_score
