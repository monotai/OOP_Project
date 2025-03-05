import pygame
import json

from sprite import SpriteSheet

try:
    with open("data.json", "r") as file:
        data = json.load(file)

    with open(data["mapData"], "r") as file:
        mapData = json.load(file)

    with open(data["plantsData"], "r") as file:
        plantsData = json.load(file)
except FileNotFoundError:
    print("Error: data.json or map data file not found")
    exit(1)
except json.JSONDecodeError:
    print("Error: Invalid JSON format in data files")
    exit(1)

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
PLANT_IMAGE = pygame.image.load(plantsData["plant"]["path"])
PLANT_IMAGE = pygame.transform.scale(PLANT_IMAGE, (SQUARE_SIZE, SQUARE_SIZE))

PLANTS = {}

try:
    PLANTS_ALL = SpriteSheet(plantsData["plants"]["path"])
    PLANTS = PLANTS_ALL.get_all_sprites(plantsData["plants"]["data"], plantsData["plants"]["size"], 2)
except KeyError as e:
    print(f"Error: Missing required key in plantsData: {e}")
    exit(1)