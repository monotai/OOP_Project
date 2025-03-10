import pygame
import sys
import os

from setting import *

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.title_font = pygame.font.Font(None, 100)  
        self.options = ["Play", "Settings", "Quit"]
        self.selected_option = 0


        audio_path = os.path.join('..', 'audio', 'best_music.mp3')
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play(-1)  

    def display_menu(self):
        self.screen.fill((0, 0, 0))
        
        title_text = self.title_font.render("Farming Simulator", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        self.screen.blit(title_text, title_rect)
        
        # Render the menu options
        for i, option in enumerate(self.options):
            color = (255, 0, 0) if i == self.selected_option else (255, 255, 255)
            text = self.font.render(option, True, color)
            rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 100))
            self.screen.blit(text, rect)
        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        if self.options[self.selected_option] == "Play":
                            print("Play selected")  
                            return "play"
                        elif self.options[self.selected_option] == "Settings":
                            print("Settings selected") 
                            return "settings"
                        elif self.options[self.selected_option] == "Quit":
                            print("Quit selected")  
                            pygame.quit()
                            sys.exit()

            self.display_menu()