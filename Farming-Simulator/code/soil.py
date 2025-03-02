import pygame
from settings import *

class SoilTile(pygame.sprite.Sprite):
    def __init__(self, pop, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pop)
        self.z = LAYERS['soil']

class Plant(pygame.sprite.Sprite):
    def __init__(self, plant_type, groups, soil, checkWatered):
        super().__init__(groups)

        self.plant_type = plant_type
        self.frames = []
        sprite_sheet = SpriteSheet(CROPS['file'])
        for i in range(CROPS_SHEET[plant_type][2]):
            frame = sprite_sheet.get_sprite(
            CROPS_SHEET[plant_type][0] + i * CROPS['width'],
            CROPS_SHEET[plant_type][1],
            CROPS['width'],
            CROPS['height']
            )
        self.frames.append(frame)
        self.soil = soil
        self.checkWatered = checkWatered

        self.age = 0
        self.maxAge = len(self.frames) - 1
        self.growSpeed = GROW_SPEED[plant_type]
        self.havest = False

        self.image = self.frames[self.age]
        self.yOffest = 0
        self.rect = self.image.get_rect(midbottom = soil.rect.midbottom + pygame.math.Vector2(0,self.y_offset))
        self.z = LAYERS['ground plant']

    def grow(self):
        if self.checkWatered(self.rect.center):
            self.age += self.growSpeed
            
        if int(self.age) > 0:
            self.z = LAYERS['main']
            #  self.hitbox = self.rect.copy().inflate(-26,-self.rect.height * 0.4)
            
        if self.age >= self.maxAge:
            self.age = self.maxAge
            self.harvestable = True
                
        self.image = self.frames[int(self.age)]
        self.rect = self.image.get_rect(midbottom = self.soil.rect.midbottom + pygame.math.Vector2(0,self.y_offset))