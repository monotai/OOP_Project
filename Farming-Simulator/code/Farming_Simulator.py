import pygame
import sys
import os

from setting import *
from level import *
from menu import Menu

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
        self.menu = Menu(self.screen)

    def run(self):
        while True:
            choice = self.menu.run()
            print(f"Menu choice: {choice}")  
            if choice == "play":
                self.play_game()
            elif choice == "settings":
                print("Settings selected")  
            else:
                print("Unknown choice")  

    def play_game(self):
        print("Starting game...")  
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    print("Starting game...")  
    game = Game()
    game.run()