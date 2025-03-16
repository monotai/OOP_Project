import pygame
import sys
import os

from setting import *
from level import *
from menu import Menu

class Game:
    def __init__(self):
        pygame.init()

        
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        
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
                self.run_settings()
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

    def run_settings(self):
        print("Settings menu...")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return  # Return to the main menu

            
            self.screen.fill((0, 0, 0))  
            pygame.display.flip()  
            self.clock.tick(60)  

if __name__ == '__main__':
    print("Starting game...")  
    game = Game()
    game.run()