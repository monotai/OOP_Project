import pygame
import os
import sys
import json
from setting import *

class Settings:
    def __init__(self):
        self.volume = 50
        self.fps = 60
        self.load_settings()

    def load_settings(self):
        try:
            with open('settings.json', 'r') as file:
                data = json.load(file)
                self.volume = data.get('volume', 50)
                self.fps = data.get('fps', 60)
        except FileNotFoundError:
            print("Settings file not found. Using default settings.")
        except json.JSONDecodeError:
            print("Error decoding settings file. Using default settings.")

    def save_settings(self):
        try:
            with open('settings.json', 'w') as file:
                json.dump({'volume': self.volume, 'fps': self.fps}, file)
        except IOError as e:
            print(f"Error saving settings: {e}")

    def __str__(self):
        return f"Settings(volume={self.volume}, fps={self.fps})"

settings = Settings()

class BaseMenu:
    def __init__(self, screen, title, options):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.title_font = pygame.font.Font(None, 100)
        self.title = title
        self.options = options
        self.selected_option = 0

        # Load background image using a relative path
        image_path = os.path.join(os.path.dirname(__file__), '..', 'graphics', 'Tiles', 'wallpaper.jpg')
        print(f"Loading background image from: {image_path}")  
        if not os.path.exists(image_path):
            print(f"Error: The file {image_path} does not exist.")
        self.background = pygame.image.load(image_path)
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

        # Load cloud images
        self.cloud_image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'graphics', 'Tiles', 'cloud.png'))
        self.cloud_image = pygame.transform.scale(self.cloud_image, (100, 50))  # Scale down the cloud image
        self.clouds = [
            {"x": -100, "y": HEIGHT // 10, "speed": 0.7},
            {"x": -200, "y": HEIGHT // 8, "speed": 0.5},
            {"x": -300, "y": HEIGHT // 6, "speed": 0.6},
            {"x": -400, "y": HEIGHT // 5, "speed": 0.4},
            {"x": -500, "y": HEIGHT // 4, "speed": 0.5},
        ]

    def animate_clouds(self):
        for cloud in self.clouds:
            cloud["x"] += cloud["speed"]  # Move the cloud to the right
            if cloud["x"] > WIDTH:
                cloud["x"] = -100  # Reset cloud position
            self.screen.blit(self.cloud_image, (cloud["x"], cloud["y"]))

    def display_menu(self):
        self.screen.blit(self.background, (0, 0))  # Display the background image

        # Animate the clouds
        self.animate_clouds()

        # Render the title with shadow
        title_text = self.title_font.render(self.title, True, (0, 0, 0))
        title_rect = title_text.get_rect(center=(WIDTH // 2 + 2, HEIGHT // 4 + 2))
        self.screen.blit(title_text, title_rect)
        title_text = self.title_font.render(self.title, True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        self.screen.blit(title_text, title_rect)

        # Render the menu options with shadow
        for i, option in enumerate(self.options):
            color = (255, 0, 0) if i == self.selected_option else (255, 255, 255)
            shadow_color = (0, 0, 0)
            text = self.font.render(option, True, shadow_color)
            rect = text.get_rect(center=(WIDTH // 2 + 2, HEIGHT // 2 + i * 100 + 2))
            self.screen.blit(text, rect)
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
                        return self.options[self.selected_option]

            self.display_menu()

class Menu(BaseMenu):
    def __init__(self, screen):
        super().__init__(screen, "Farming Simulator", ["Play", "Settings", "Quit"])

    def run(self):
        while True:
            choice = super().run()
            if choice == "Play":
                return "play"
            elif choice == "Settings":
                return "settings"
            elif choice == "Quit":
                pygame.quit()
                sys.exit()

class SettingsMenu(BaseMenu):
    def __init__(self, screen):
        super().__init__(screen, "Settings", ["Sound", "FPS", "Back"])

    def run(self):
        while True:
            choice = super().run()
            if choice == "Back":
                settings.save_settings()  # Save settings when exiting
                return
            elif choice == "Sound":
                sound_menu = SoundMenu(self.screen)
                sound_menu.run()
            elif choice == "FPS":
                fps_menu = FPSMenu(self.screen)
                fps_menu.run()

class SoundMenu(BaseMenu):
    def __init__(self, screen):
        super().__init__(screen, "Sound Settings", [f"Volume: {settings.volume}", "Back"])

    def run(self):
        while True:
            choice = super().run()
            if choice == "Back":
                return
            elif choice.startswith("Volume"):
                settings.volume = (settings.volume + 10) % 110
                self.options[0] = f"Volume: {settings.volume}"
                pygame.mixer.music.set_volume(settings.volume / 100.0)  # Set the mixer volume

class FPSMenu(BaseMenu):
    def __init__(self, screen):
        super().__init__(screen, "FPS Settings", [f"FPS: {settings.fps}", "Back"])

    def run(self):
        while True:
            choice = super().run()
            if choice == "Back":
                return
            elif choice.startswith("FPS"):
                settings.fps = (settings.fps + 10) % 120
                self.options[0] = f"FPS: {settings.fps}"