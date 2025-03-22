import pygame
from pygame import mixer

from setting import *
from sprites import *
from t import Timer

class Level:
    def __init__(self):
        self.surface = pygame.display.get_surface()

        self.all_plants = pygame.sprite.Group()

        self.center = (self.surface.get_width() // 2, self.surface.get_height() // 2)

        self.plantNum = 0
        self.last_key_time = 0
        self.key_cooldown = 200  # milliseconds

        self.timer = Timer(1000)
        self.timer.activate()
        self.mouse_pressed = False

        self.board = BOARD

        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)  # Smaller font for crop names

        pygame.mixer.music.load('../audio/best_music.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1, 0.0, 0)

        self.plantSound = pygame.mixer.Sound('../audio/plant.wav')
        self.plantSound.set_volume(0.1)

        self.hoeSound = pygame.mixer.Sound('../audio/hoe.wav')
        self.hoeSound.set_volume(0.1)

        self.money = 0

        # Load block image for frame
        self.block_image = pygame.image.load('../graphics/Other/block.png')
        self.block_image = pygame.transform.scale(self.block_image, (150, 50))

        # test menu
        self.font = pygame.font.Font(None, 36)
        self.menuMode = False
        self.menuNum = 0
        self.all_boxs = pygame.sprite.Group()
        self.contain = Container(self.all_boxs, (0, 0), (500, 500), (255, 255, 255))
        self.contain.set_center(self.center)
        self.contain.create_child((500, 200), (255, 0, 0))
        self.contain.create_child((500, 200), (0, 255, 0))
        self.contain.create_child((500, 200), (0, 0, 255))

        # work with file
        self.hasData = False
        self.time = 0
        self.dataFile = FileJson('../data/Plant_Data.json')

    def mark_square(self, row, col, player):
        self.board[row][col] = player

    def available_square(self, row, col):
        if 0 <= row < BOARD_ROWS and 0 <= col < BOARD_COLS and self.board[row][col] == 0:
            return True
        return False

    def find_sprite_at_position(self, group, position):
        for plant in group:
            if plant.rect[0] == position[0] and plant.rect[1] == position[1]:
                return plant
        return None

    def get_key_by_index(self):
        num = self.plantNum
        for plant_sheet in PLANTS.keys():
            if num == 0:
                return plant_sheet
            num -= 1

    def get_crop_name_by_index(self):
        return PLANTS_DATA[self.get_key_by_index()]["Name"]

    def draw_text_with_frame(self, text, position, font, text_color, draw_frame=True):
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect()
        frame_rect = self.block_image.get_rect()

        # Scale the frame to fit the text
        frame_rect.width = text_rect.width + 70  # Increase the width
        frame_rect.height = text_rect.height + 20
        frame_image = pygame.transform.scale(self.block_image, (frame_rect.width, frame_rect.height))

        # Position the text and frame to the top right of the crop
        frame_rect.topleft = (position[0], position[1] - frame_rect.height - 30)
        text_rect.center = frame_rect.center

        if draw_frame:
            self.surface.blit(frame_image, frame_rect)
        self.surface.blit(text_surface, text_rect)

    def input(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        current_time = pygame.time.get_ticks()

        if not self.menuMode:
            if current_time - self.last_key_time > self.key_cooldown:
                if keys[pygame.K_RIGHT]:
                    self.plantNum += 1
                    if self.plantNum > len(PLANTS) - 1:
                        self.plantNum = 0
                    self.last_key_time = current_time
                elif keys[pygame.K_LEFT]:
                    self.plantNum -= 1
                    if self.plantNum < 0:
                        self.plantNum = len(PLANTS) - 1
                    self.last_key_time = current_time
                elif keys[pygame.K_TAB]:
                    self.menuMode = True

            if mouse[0] and not self.mouse_pressed:
                self.mouse_pressed = True
                pos = pygame.mouse.get_pos()
                mouseX = pos[0]
                mouseY = pos[1]

                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                posSripte = ((clicked_col) * SQUARE_SIZE, (clicked_row - 1) * SQUARE_SIZE)
                print(clicked_row, clicked_col)
                # plant
                name = PLANTS_DATA[self.get_key_by_index()]["Name"]
                if self.available_square(clicked_row, clicked_col):
                    self.plantSound.play()
                    self.mark_square(clicked_row, clicked_col, self.get_key_by_index())
                    plant = Plant(posSripte, self.get_key_by_index(), 1)
                    self.all_plants.add(plant)

                    # input to file
                    if self.dataFile.data.get(f"{self.time}") is None:
                        self.dataFile.data[f"{self.time}"] = {"plant": {}}
                        self.dataFile.data[f"{self.time}"]["plant"][name] = 1
                    else:
                        if self.dataFile.data[f"{self.time}"].get("plant") is None:
                            self.dataFile.data[f"{self.time}"]["plant"] = {}
                        if name in self.dataFile.data[f"{self.time}"]["plant"].keys():
                            self.dataFile.data[f"{self.time}"]["plant"][name] += 1
                        else:
                            self.dataFile.data[f"{self.time}"]["plant"][name] = 1
                    self.dataFile.update()
                    self.hasData = True
                    # fix image
                    if not self.available_square(clicked_row + 1, clicked_col):
                        sprite = self.find_sprite_at_position(self.all_plants, (posSripte[0], posSripte[1] + SQUARE_SIZE))

                        if sprite is not None:
                            plant = Plant(sprite.pos, sprite.key, sprite.frame)
                            sprite.kill()
                            self.all_plants.add(plant)
                # harvest
                else:
                    sprite = self.find_sprite_at_position(self.all_plants, posSripte)
                    if sprite is not None:
                        if sprite.is_harvest():
                            # harvest to file
                            if self.dataFile.data.get(f"{self.time}") is None:
                                self.dataFile.data[f"{self.time}"] = {"harvest": {}}
                                self.dataFile.data[f"{self.time}"]["harvest"][name] = sprite.harvestPrice
                            else:
                                if self.dataFile.data[f"{self.time}"].get("harvest") is None:
                                    self.dataFile.data[f"{self.time}"]["harvest"] = {}

                                if name in self.dataFile.data[f"{self.time}"]["harvest"].keys():
                                    self.dataFile.data[f"{self.time}"]["harvest"][name] += sprite.harvestPrice
                                else:
                                    self.dataFile.data[f"{self.time}"]["harvest"][name] = sprite.harvestPrice

                            self.dataFile.data[f"{self.time}"]["harvest"]["money"] = self.money
                            self.dataFile.update()

                            self.hoeSound.play()
                            self.money += sprite.harvestPrice

                            if not sprite.harvest_time():
                                self.mark_square(clicked_row, clicked_col, 0)
                                sprite.kill()

            elif not mouse[0]:
                self.mouse_pressed = False
        elif current_time - self.last_key_time > self.key_cooldown:
            if keys[pygame.K_RIGHT]:
                if self.menuNum < len(self.dataFile.data):
                    self.menuNum += 1
            elif keys[pygame.K_LEFT]:
                if self.menuNum > 0:
                    self.menuNum -= 1
            elif keys[pygame.K_TAB]:
                self.menuMode = False

    def run(self):
        self.surface.fill('black')
        self.input()
        self.surface.blit(MAP_IMAGE, (0, 0))

        if len(self.all_plants) > 0:
            if not self.timer.update():
                self.time += 1
                for plant in self.all_plants:
                    plant.update()
                self.timer.activate()
            self.all_plants.draw(self.surface)

        self.surface.blit(BLOCK, (0, 0))
        self.money_text = self.font.render(f'{self.money}', True, (255, 255, 255))
        self.money_rect = self.money_text.get_rect(topright=(self.surface.get_width() - 10, 10))
        self.surface.blit(self.money_text, self.money_rect)
        self.surface.blit(SEED[self.get_key_by_index()][0], (10, 11))

        # Display crop name
        crop_name = self.get_crop_name_by_index()
        self.draw_text_with_frame(crop_name, (85, 75), self.small_font, (0, 0, 0))

    def menu(self):
        if self.hasData:
            information = self.dataFile.data[f"{self.menuNum}"]
            self.box.add_text(f"{information}", self.font, (0, 0, 0))
        self.all_boxs.draw(self.surface)

    def test(self):
        self.all_boxs.update()
        self.all_boxs.draw(self.surface)