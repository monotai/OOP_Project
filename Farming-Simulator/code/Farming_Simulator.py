import os
import pygame
import sys
from setting import *
from level import *
from menu import Menu, SettingsMenu

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
                self.run_settings_menu()
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

    def run_settings_menu(self):
        settings_menu = SettingsMenu(self.screen)
        settings_menu.run()

    def run_settings(self):
        print("Settings menu...")
        font = pygame.font.Font(None, 36)
        header_font = pygame.font.Font(None, 40)
        
        # Load background image using a relative path
        image_path = os.path.join(os.path.dirname(__file__), '..', 'graphics', 'Tiles', 'wallpaper.jpg')
        print(f"Loading background image from: {image_path}")  
        if not os.path.exists(image_path):
            print(f"Error: The file {image_path} does not exist.")
        background = pygame.image.load(image_path)
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        
        # Create a semi-transparent overlay
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(128)  # Set transparency level (0-255)
        overlay.fill((0, 0, 0))  # Fill with black color
        
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
        
        # Render the player data as a table
        def render_crop_data():
            texts = []
            y_offset = 100
            header_text = header_font.render('Crop Data', True, (255, 255, 255))
            header_rect = header_text.get_rect(center=(self.screen.get_width() // 2, 50))
            texts.append((header_text, header_rect))
            table_headers = ['Crop', 'Seeds Planted', 'Price Harvested']
            header_x_positions = [self.screen.get_width() // 4, self.screen.get_width() // 2, 3 * self.screen.get_width() // 4]
            for i, header in enumerate(table_headers):
                header_text = font.render(header, True, (255, 255, 255))
                header_rect = header_text.get_rect(center=(header_x_positions[i], y_offset))
                texts.append((header_text, header_rect))
            y_offset += 40
            for crop, data in crop_data.items():
                crop_text = font.render(crop, True, (255, 255, 255))
                crop_rect = crop_text.get_rect(center=(self.screen.get_width() // 4, y_offset))
                texts.append((crop_text, crop_rect))

                seeds_text = font.render(str(data["seeds_planted"]), True, (255, 255, 255))
                seeds_rect = seeds_text.get_rect(center=(self.screen.get_width() // 2, y_offset))
                texts.append((seeds_text, seeds_rect))

                price_text = font.render(f'${data["price_harvested"]}', True, (255, 255, 255))
                price_rect = price_text.get_rect(center=(3 * self.screen.get_width() // 4, y_offset))
                texts.append((price_text, price_rect))

                y_offset += 40
            return texts

        def update_crop_data():
            crop_data.clear()
            if self.level.dataFile.data:
                for key in self.level.dataFile.data:
                    if "plant" in self.level.dataFile.data[key]:
                        for crop, amount in self.level.dataFile.data[key]["plant"].items():
                            if crop not in crop_data:
                                crop_data[crop] = {"seeds_planted": 0, "price_harvested": 0}
                            crop_data[crop]["seeds_planted"] += amount
                    if "harvest" in self.level.dataFile.data[key]:
                        for crop, harvested_price in self.level.dataFile.data[key]["harvest"].items():
                            if crop == "money":
                                continue  # Skip the "money" crop type
                            if crop not in crop_data:
                                crop_data[crop] = {"seeds_planted": 0, "price_harvested": 0}
                            crop_data[crop]["price_harvested"] += harvested_price

        texts = render_crop_data()
        scroll_offset = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return  # Return to the main menu
                    elif event.key == pygame.K_DOWN:
                        scroll_offset += 10  # Scroll down
                    elif event.key == pygame.K_UP:
                        scroll_offset -= 10  # Scroll up
                        if scroll_offset < 0:
                            scroll_offset = 0  # Prevent scrolling above the crop data
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 5:  # Mouse wheel down
                        scroll_offset += 10
                    elif event.button == 4:  # Mouse wheel up
                        scroll_offset -= 10
                        if scroll_offset < 0:
                            scroll_offset = 0  # Prevent scrolling above the crop data

            update_crop_data()
            texts = render_crop_data()

            self.screen.blit(background, (0, 0))  # Display the background image
            self.screen.blit(overlay, (0, 0))  # Display the semi-transparent overlay
            for text, rect in texts:
                rect.y -= scroll_offset  # Apply the scroll offset
                self.screen.blit(text, rect)  # Draw the crop data text
            pygame.display.flip()  
            self.clock.tick(60)  

if __name__ == '__main__':
    print("Starting game...")  
    game = Game()
    game.run()