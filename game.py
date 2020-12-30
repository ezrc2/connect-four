import sys
import pygame

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

EMPTY = 0
HUMAN = 1
COMPUTER = 2

ROWS = 6
COLUMNS = 7

SQUARE_SIZE = 100
CIRCLE_RADIUS = 40

class ConnectFour:

    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((700, 600))
        pygame.display.set_caption("Connect Four")

        self.board = [[EMPTY for j in range(COLUMNS)] for i in range(ROWS)]
        self.human_turn = True

    def run_game_loop(self):
        clock = pygame.time.Clock()
        while True:
            self.draw_board()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_click(event)

            pygame.display.update()
            clock.tick(60)

    def draw_board(self):
        pygame.draw.rect(self.display, BLUE, (0, 0, COLUMNS * SQUARE_SIZE, ROWS * SQUARE_SIZE))

        for i in range(ROWS):
            for j in range(COLUMNS):
                center = (j * SQUARE_SIZE + 0.5 * SQUARE_SIZE, i * SQUARE_SIZE + 0.5 * SQUARE_SIZE)
                if self.board[i][j] == 0:
                    color = WHITE
                elif self.board[i][j] == HUMAN:
                    color = RED
                elif self.board[i][j] == COMPUTER:
                    color = YELLOW
                pygame.draw.circle(self.display, color, center, CIRCLE_RADIUS)

    def drop_piece(self, column, player):
        for i in range(ROWS - 1, -1, -1):
            if self.board[i][column] == EMPTY:
                self.board[i][column] = player
                break

    def handle_mouse_click(self, event):
        mouse_x = event.pos[0]
        for j in range(COLUMNS):
            if j * SQUARE_SIZE <= mouse_x < (j + 1) * SQUARE_SIZE:
                if self.human_turn:
                    self.drop_piece(j, HUMAN)
                    self.human_turn = not self.human_turn
                    break
                else:
                    self.drop_piece(j, COMPUTER)
                    self.human_turn = not self.human_turn

if __name__ == "__main__":
    ConnectFour().run_game_loop()
