import pygame
import json

from support import *

try:
    with open("data.json", "r") as file:
        data = json.load(file)

    with open(data["mapData"], "r") as file:
        mapData = json.load(file)

    with open(data["plantsData"], "r") as file:
        plantsData = json.load(file)
    with open(data["hoeDirtsData"], "r") as file:
        hoeData = json.load(file)
except FileNotFoundError:
    print("Error: data.json or map data file not found")
    exit(1)
except json.JSONDecodeError:
    print("Error: Invalid JSON format in data files")
    exit(1)

FPS = 60

CAPTION = data["caption"]
SIZE = data["mapsize"]
WIDTH, HEIGHT = mapData["size"][0] * SIZE, mapData["size"][1] * SIZE
SQUARE_SIZE = data["squarSize"]
BOARD_ROWS = HEIGHT // SQUARE_SIZE
BOARD_COLS = WIDTH // SQUARE_SIZE
BOARD = mapData["collotion"]

BLOCK = pygame.image.load(data["blockPath"])
BLOCK = pygame.transform.scale(BLOCK, (SQUARE_SIZE + 20, SQUARE_SIZE*2 + 20))

MAP_IMAGE = pygame.image.load(mapData["path"])
MAP_IMAGE = pygame.transform.scale(MAP_IMAGE, (WIDTH, HEIGHT))

PLANTS = {}

PLANTS_SHEET = SpriteSheet(plantsData["plants"]["path"])
PLANTS = PLANTS_SHEET.get_all_sprites(plantsData["plants"]["data"], (SQUARE_SIZE, SQUARE_SIZE * 2), plantsData["plants"]["size"])

HOE_DIRTS = {}

# DIRT_SPRITE_SHEET = SpriteSheet(hoeData["path"])
# HOE_DIRTS["small"] = DIRT_SPRITE_SHEET.get_all_sprites(he)


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