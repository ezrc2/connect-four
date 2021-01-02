import math

EMPTY = 0
HUMAN_PLAYER = 1
AI_PLAYER = 2

class Minimax():

    def __init__(self):
        self.depth = 4

    def find_move(self, board):
        move, score = self.minimax(board, self.depth, True)
        return move

    def get_heuristic(self, board):
        heuristic = 0

 

        return heuristic


    def is_terminal(self, board):
        return board.won_game(HUMAN_PLAYER) or board.won_game(AI_PLAYER) or board.is_full()

    def minimax(self, board, depth, maximizing):
        if depth == 0:
            return -1, self.get_heuristic(board)
        elif self.is_terminal(board):
            if board.won_game(AI_PLAYER):
                return -1, math.inf
            elif board.won_game(HUMAN_PLAYER):
                return -1, -math.inf
            else:
                return -1, 0

        if maximizing:
            pass



        return 0
