import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 320, 320
SQUARE_SIZE = 32
BOARD_ROWS, BOARD_COLS = 10, 10

# Load images
MAP_IMAGE = pygame.image.load('./graphics/map_0.png')
PLANT_IMAGE = pygame.image.load('./graphics/plant.png')
PLANT_IMAGE = pygame.transform.scale(PLANT_IMAGE, (SQUARE_SIZE, SQUARE_SIZE))

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Farming Simulator')

# Board
board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]

# Draw figures
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'plant':
                screen.blit(PLANT_IMAGE, (col * SQUARE_SIZE, row * SQUARE_SIZE))

# Mark square
def mark_square(row, col, player):
    board[row][col] = player

# Check if square is available
def available_square(row, col):
    return board[row][col] is None

# Main loop
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, 'plant')
                draw_figures()

    screen.blit(MAP_IMAGE, (0, 0))
    draw_figures()
    pygame.display.update()
