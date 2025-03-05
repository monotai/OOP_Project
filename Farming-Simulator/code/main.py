import pygame
import sys

from setting import *

class Game:
    def __init__(self):
        pygame.init()

        # Screen setup
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()

        # Board
        self.board = BOARD
        print(len(self.board))
        print(len(self.board[0]))
        self.game_over = False

        self.plantNum = 1


    def draw_figures(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if str(self.board[row][col]).find("p") != -1:
                    num = int(self.board[row][col].replace("p_", ""))
                    self.screen.blit(PLANTS[f"{num}"][0], (col * SQUARE_SIZE, (row-1) * SQUARE_SIZE))

    def mark_square(self, row, col, player):
        self.board[row][col] = player

    def available_square(self, row, col):
        return self.board[row][col] == 0

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.plantNum += 1
                        if self.plantNum > len(PLANTS):
                            self.plantNum = 1
                    elif event.key == pygame.K_LEFT:
                        self.plantNum -= 1
                        if self.plantNum < 1:
                            self.plantNum = len(PLANTS)

                if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]

                    clicked_row = mouseY // SQUARE_SIZE
                    clicked_col = mouseX // SQUARE_SIZE

                    if self.available_square(clicked_row, clicked_col):
                        self.mark_square(clicked_row, clicked_col, f'p_{self.plantNum}')

            self.screen.blit(MAP_IMAGE, (0, 0))
            self.draw_figures()
            self.screen.blit(BLOCK, (0, 0))
            self.screen.blit(PLANTS[f"{self.plantNum}"][0], (10, 10))
            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()
