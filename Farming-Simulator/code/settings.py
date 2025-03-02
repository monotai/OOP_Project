from pygame.math import Vector2
import pygame
# screen in pixel
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TILE_SIZE = 64 # size of block in game

class SpriteSheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey('black')
        return sprite

# overlay positions 

PLAYER_TOOL_OFFSET = {
	'left': Vector2(-50,40),
	'right': Vector2(50,40),
	'up': Vector2(0,-10),
	'down': Vector2(0,50)
}
# level of rander every textures
LAYERS = {
	'water': 0,
	'ground': 1,
	'soil': 2,
	'soil water': 3,
	'rain floor': 4,
	'house bottom': 5,
	'ground plant': 6,
	'main': 7,
	'house top': 8,
	'fruit': 9,
	'rain drops': 10
}
# size of apple
APPLE_POS = {
	'Small': [(18,17), (30,37), (12,50), (30,45), (20,30), (30,10)],
	'Large': [(30,24), (60,65), (50,50), (16,40),(45,50), (42,70)]
}
# speed of grow
GROW_SPEED = {
	'plant': 1
}
# price of selling
SALE_PRICES = {
	'wood': 4,
	'apple': 2,
	'corn': 10,
	'tomato': 20
}
# seed price
PURCHASE_PRICES = {
	'corn': 4,
	'tomato': 5
}

# plante sheet
CROPS = {
    'file': '../graphics/crops.png',
    'width': 16,
    'height': 32
}
CROPS_SHEET = {
    'plant': [0, 0, 6] # x, y, and size of grown
}