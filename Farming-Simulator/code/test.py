import pygame
import sys
import os

from setting import *
from level import *

class Game:
    def __init__(self):
        pygame.init()

        # Center the window
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        # Screen setup
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.level.dataFile.update()
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DELETE:
                        pygame.quit()
                        sys.exit()

            self.level.test()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
