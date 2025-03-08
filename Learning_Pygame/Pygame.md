<center><h1>Pygame Tuitorial</h1><center>

# Tic Tac Toe

- basic window

```
# main.py
import pygame

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

run = True:
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUTI():
			run = False

pygame.quit()
```

- set background and grid

```
LINE_WIDTH = 6
def draw_grid():
	bg = (255, 255, 200)
	grid = (50, 50, 50)
	screen.fill(bg)
	for x in range(1, 3):
		pygame.draw.line(screen, grid, (0, x*100), (SCREEN_WIDTH, x *100), LINE_WIDTH)
		pygame.draw.line(screen, grid, (x*100, 0), (x*100, SCREEN_HEIGHT), LINE_WIDTH)
```
