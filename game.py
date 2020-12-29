import sys
import pygame

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

ROWS = 6
COLUMNS = 7
SQUARE_SIZE = 100
CIRCLE_RADIUS = 40

class ConnectFour:

    def __init__(self):
        pygame.display.init()
        self.display = pygame.display.set_mode((700, 600))
        pygame.display.set_caption("Connect Four")

        self.board = [[0 for j in range(COLUMNS)] for i in range(ROWS)]

    def draw_board(self):
        pygame.draw.rect(self.display, BLUE, (0, 0, COLUMNS * SQUARE_SIZE, ROWS * SQUARE_SIZE))

        for i in range(ROWS):
            for j in range(COLUMNS):
                center = (j * SQUARE_SIZE + 0.5 * SQUARE_SIZE, i * SQUARE_SIZE + 0.5 * SQUARE_SIZE)
                if self.board[i][j] == 0:
                    color = WHITE
                elif self.board[i][j] == 1:
                    color = RED
                elif self.board[i][j] == 2:
                    color = YELLOW
                pygame.draw.circle(self.display, color, center, CIRCLE_RADIUS)


def main():
    pygame.init()
    game = ConnectFour()
    clock = pygame.time.Clock()
    while True:
        game.draw_board()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
