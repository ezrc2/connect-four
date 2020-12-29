import pygame

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
SQUARE_SIZE = 100

class ConnectFour:

    def __init__(self):
        pygame.display.init()
        self.display = pygame.display.set_mode((700, 600))
        pygame.display.set_caption("Connect Four")
        
        self.rows = 6
        self.columns = 7
        self.board = [[0 for j in range(self.columns)] for i in range(self.rows)]




if __name__ == "__main__":
    a = ConnectFour()
    