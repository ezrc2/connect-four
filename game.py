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
HUMAN_PLAYER = 1
AI_PLAYER = 2

ROWS = 6
COLUMNS = 7

LINE_WIDTH = 3
SQUARE_SIZE = 100
CIRCLE_RADIUS = 40

class ConnectFour:

    def __init__(self):
        pygame.init()
        pygame.display.init()
        pygame.font.init()
        self.display = pygame.display.set_mode((COLUMNS * SQUARE_SIZE, (ROWS + 1) * SQUARE_SIZE))
        pygame.display.set_caption("Connect Four")
        self.font = pygame.font.SysFont("Consolas", 90)

        self.board = Board(EMPTY, ROWS, COLUMNS)
        self.ai = Minimax()
        
        self.human_turn = True

    def run_game_loop(self):
        clock = pygame.time.Clock()
        game_over = False
        while not game_over:
            self.draw_board()

            if self.board.won_game(HUMAN_PLAYER) or self.board.won_game(AI_PLAYER):
                if self.board.won_game(HUMAN_PLAYER):
                    text = self.font.render("You win!", True, BLACK)
                else:
                    text = self.font.render("You lose!", True, BLACK)

                text_rect = text.get_rect(center=(SQUARE_SIZE * COLUMNS / 2, SQUARE_SIZE / 2))
                self.display.blit(text, text_rect)

                game_over = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if self.human_turn and event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_click(event.pos[0])

            if not self.human_turn:
                self.board.drop_piece(0, AI_PLAYER)
                self.human_turn = True

            if not game_over:
                self.draw_next_piece(pygame.mouse.get_pos()[0])

            pygame.display.update()
            clock.tick(60)

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
                if self.board.board[i][j] == 0:
                    color = WHITE
                elif self.board.board[i][j] == HUMAN_PLAYER:
                    color = RED
                elif self.board.board[i][j] == AI_PLAYER:
                    color = YELLOW

                pygame.draw.circle(self.display, color, center, CIRCLE_RADIUS)
                pygame.draw.circle(self.display, BLACK, center, CIRCLE_RADIUS, LINE_WIDTH)

    def draw_next_piece(self, mouse_x):
        column = mouse_x // SQUARE_SIZE
        center = ((column + 0.5) * SQUARE_SIZE, SQUARE_SIZE / 2)
        pygame.draw.circle(self.display, RED, center, CIRCLE_RADIUS)

    def handle_mouse_click(self, mouse_x):
        column = mouse_x // SQUARE_SIZE
        if self.human_turn:
            self.board.drop_piece(column, HUMAN_PLAYER)
            self.human_turn = False


if __name__ == "__main__":
    ConnectFour().run_game_loop()
