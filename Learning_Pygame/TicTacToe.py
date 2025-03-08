import pygame

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HIEGHT = 300
CELL_WIDTH = 100

GREEN = (0, 255, 0)
RED = (255, 0, 0)

pos = []
player = 1

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIEGHT))
pygame.display.set_caption('Tic Tac Toe')

LINE_WIDTH = 6

def draw_grid():
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, x*CELL_WIDTH), (SCREEN_WIDTH,  x*CELL_WIDTH), LINE_WIDTH)
        pygame.draw.line(screen, grid, (x*CELL_WIDTH, 0), (x*CELL_WIDTH, SCREEN_HIEGHT), LINE_WIDTH)

marker = []

for x in range(3):
    row = [0]*3
    marker.append(row)

def draw_marker():
    x_pos = 0
    for x in marker:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, GREEN, x_pos * SC)


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            cliked = True
        if event.type == pygame.MOUSEBUTTONUP and cliked == True:
            cliked = False
            pos = pygame.mouse.get_pos()
            cell_x = pos[0] // CELL_WIDTH
            cell_y = pos[1] // CELL_WIDTH

            if marker[cell_x][cell_y] == 0:
                marker[cell_x][cell_y] = player
                player *= -1

 
    draw_grid()
    pygame.display.update()

pygame.quit()
