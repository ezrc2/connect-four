import sys
import pygame
from minimax import Minimax
from board import Board

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREY = (150, 150, 150)

EMPTY = 0
HUMAN_PIECE = 1
AI_PIECE = 2

ROWS = 6
COLUMNS = 7

LINE_WIDTH = 3
SQUARE_SIZE = 100
CIRCLE_RADIUS = 40

DEPTH = 4

class ConnectFour:

    def __init__(self):
        pygame.init()
        pygame.display.init()
        pygame.font.init()
        self.display = pygame.display.set_mode((COLUMNS * SQUARE_SIZE, (ROWS + 1) * SQUARE_SIZE))
        pygame.display.set_caption("Connect Four")
        self.font = pygame.font.SysFont("Consolas", 90)

        self.board = Board(EMPTY, ROWS, COLUMNS)
        self.ai_player = Minimax(DEPTH)
        self.human_turn = True

    def run_game_loop(self):
        game_over = False
        while not game_over:
            self.draw_board()

            if self.board.is_full() or self.board.won_game(HUMAN_PIECE) or self.board.won_game(AI_PIECE):
                self.show_end_message()
                game_over = True

            valid_columns = self.board.get_valid_columns()
            mouse_column = pygame.mouse.get_pos()[0] // SQUARE_SIZE

            if not game_over:
                self.draw_next_piece(mouse_column)

            pygame.display.update()

            if not game_over:
                if self.human_turn:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN and mouse_column in valid_columns:
                            self.board.drop_piece(mouse_column, HUMAN_PIECE)
                            self.human_turn = False
                else:
                    ai_move = self.ai_player.find_move(self.board)
                    self.board.drop_piece(ai_move, AI_PIECE)
                    self.human_turn = True

            pygame.display.update()

        if game_over:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

    def draw_board(self):
        pygame.draw.rect(self.display, BLUE, (0, SQUARE_SIZE, COLUMNS * SQUARE_SIZE, (ROWS + 1) * SQUARE_SIZE))
        pygame.draw.rect(self.display, WHITE, (0, 0, COLUMNS * SQUARE_SIZE, SQUARE_SIZE))

        for i in range(ROWS):
            for j in range(COLUMNS):
                center = ((j  +  0.5) * SQUARE_SIZE, (i  +  1.5) * SQUARE_SIZE)
                piece = self.board.get_piece(i, j)
                if piece == 0:
                    color = WHITE
                elif piece == HUMAN_PIECE:
                    color = RED
                elif piece == AI_PIECE:
                    color = YELLOW

                pygame.draw.circle(self.display, color, center, CIRCLE_RADIUS)
                pygame.draw.circle(self.display, BLACK, center, CIRCLE_RADIUS, LINE_WIDTH) # circle outline

    def draw_next_piece(self, column):
        center = ((column + 0.5) * SQUARE_SIZE, SQUARE_SIZE / 2)
        pygame.draw.circle(self.display, RED, center, CIRCLE_RADIUS)

    def show_end_message(self):
        if self.board.won_game(HUMAN_PIECE):
            text = self.font.render("You win!", True, BLACK)
        elif self.board.won_game(AI_PIECE):
            text = self.font.render("You lose!", True, BLACK)
        else:
            text = self.font.render("Tie", True, BLACK)

        text_rect = text.get_rect(center=(SQUARE_SIZE * COLUMNS / 2, SQUARE_SIZE / 2))
        self.display.blit(text, text_rect)


if __name__ == "__main__":
    ConnectFour().run_game_loop()
