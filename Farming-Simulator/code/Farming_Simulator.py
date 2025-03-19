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
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:  # Press 'S' key to show settings
                        self.run_settings()

            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

    def run_settings(self):
        print("Settings menu...")
        font = pygame.font.Font(None, 36)
        
        # Access player data from the level instance
        crop_data = {}
        if self.level.dataFile.data:
            for key in self.level.dataFile.data:
                print(f"Processing key: {key}")  # Debug print
                if "plant" in self.level.dataFile.data[key]:
                    for crop, amount in self.level.dataFile.data[key]["plant"].items():
                        if crop not in crop_data:
                            crop_data[crop] = {"seeds_planted": 0, "price_harvested": 0}
                        crop_data[crop]["seeds_planted"] += amount
                        print(f"Added {amount} seeds for crop {crop}")  # Debug print
                if "harvest" in self.level.dataFile.data[key]:
                    for crop, harvested_price in self.level.dataFile.data[key]["harvest"].items():
                        if crop == "money":
                            continue  # Skip the "money" crop type
                        if crop not in crop_data:
                            crop_data[crop] = {"seeds_planted": 0, "price_harvested": 0}
                        crop_data[crop]["price_harvested"] += harvested_price
                        print(f"Added ${harvested_price} to crop {crop}")  # Debug print
                else:
                    print(f"No harvest data for key: {key}")  # Debug print
        
        # Render the player data as text
        texts = []
        y_offset = -40
        for crop, data in crop_data.items():
            crop_text = font.render(f'Crop: {crop}, Seeds Planted: {data["seeds_planted"]}, Price Harvested: ${data["price_harvested"]}', True, (255, 255, 255))
            crop_rect = crop_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + y_offset))
            texts.append((crop_text, crop_rect))
            y_offset += 40

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return  # Return to the main menu

            self.screen.fill((0, 0, 0))  
            for text, rect in texts:
                self.screen.blit(text, rect)  # Draw the crop data text
            pygame.display.flip()  
            self.clock.tick(60)  

if __name__ == '__main__':
    print("Starting game...")  
    game = Game()
    game.run()