import pygame
import json

from support import *

with open("data.json", "r") as file:
    dataForSprite = json.load(file)

with open(dataForSprite["mapData"], "r") as file:
    mapData = json.load(file)

with open(dataForSprite["plantsData"], "r") as file:
    plantsData = json.load(file)
with open(dataForSprite["hoeDirtsData"], "r") as file:
    hoeData = json.load(file)
with open(dataForSprite["Plants_Data_Stradew"]) as file:
    plants_stradew = json.load(file)


FPS = 60

CAPTION = dataForSprite["caption"]
SIZE = dataForSprite["mapsize"]
WIDTH, HEIGHT = mapData["size"][0] * SIZE, mapData["size"][1] * SIZE
SQUARE_SIZE = dataForSprite["squarSize"]
BOARD_ROWS = HEIGHT // SQUARE_SIZE
BOARD_COLS = WIDTH // SQUARE_SIZE
BOARD = mapData["collotion"]

BLOCK = pygame.image.load(dataForSprite["blockPath"])
BLOCK = pygame.transform.scale(BLOCK, (SQUARE_SIZE + 20, SQUARE_SIZE + 20))

MAP_IMAGE = pygame.image.load(mapData["path"])
MAP_IMAGE = pygame.transform.scale(MAP_IMAGE, (WIDTH, HEIGHT))

MORNEY = pygame.image.load(dataForSprite["Money_Image"])
MORNEY = pygame.transform.scale(MORNEY, (130, 28))
 
PLANTS = {}

PLANTS_SHEET = SpriteSheet(plants_stradew["Crops_Image"]["path"])

dataForSprite = {}
copy_json_by_key(plants_stradew["Crops"], dataForSprite, "Frames", "frames")
copy_json_by_key(plants_stradew["Crops"], dataForSprite, "SpriteIndex_Crop", "index")

PLANTS = PLANTS_SHEET.get_all_sprites_by_index(dataForSprite, plants_stradew["Crops_Image"]["size"][0], (8, 1), plants_stradew["Crops_Image"]["sprite_size"], [SQUARE_SIZE, SQUARE_SIZE*2])

PLANTS_DATA = {}
copy_json_by_key(plants_stradew["Crops"], PLANTS_DATA, "Name", "Name")
copy_json_by_key(plants_stradew["Crops"], PLANTS_DATA, "Price", "Price")
copy_json_by_key(plants_stradew["Crops"], PLANTS_DATA, "HarvestName", "HarvestName")
copy_json_by_key(plants_stradew["Crops"], PLANTS_DATA, "HarvestPrice", "HarvestPrice")
copy_json_by_key(plants_stradew["Crops"], PLANTS_DATA, "DaysInPhase", "DaysInPhase")
copy_json_by_key(plants_stradew["Crops"], PLANTS_DATA, "RegrowDays", "RegrowDays")
copy_json_by_key(plants_stradew["Crops"], PLANTS_DATA, "TintColors", "TintColors")

ITEMS_SHEET = SpriteSheet(plants_stradew["Items_image"]["path"])

dataForSprite = {}
copy_json_by_key(plants_stradew["Crops"], dataForSprite, "SpriteIndex_Seed", "index")
SEED = ITEMS_SHEET.get_all_sprites_by_index(dataForSprite, plants_stradew["Items_image"]["size"][0], (1, 1), plants_stradew["Items_image"]["sprite_size"], [SQUARE_SIZE, SQUARE_SIZE], 1)

# DIRT_SPRITE_SHEET = SpriteSheet(hoeData["path"])
# HOE_DIRTS["small"] = DIRT_SPRITE_SHEET.get_all_sprites(he)

#ITEMS_IMAGE_SHEET = SpriteSheet()