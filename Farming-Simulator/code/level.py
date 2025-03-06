import pygame

from setting import *
from sprites import *
from t import Timer

class Level:
	def __init__(self):
		self.surface = pygame.display.get_surface()

		self.all_plants = pygame.sprite.Group()

		self.plantNum = 1
		self.last_key_time = 0
		self.key_cooldown = 200  # milliseconds

		self.timer = Timer(1000)
		self.timer.activate()

		self.board = BOARD
		
	def mark_square(self, row, col, player):
		self.board[row][col] = player

	def available_square(self, row, col):
		return self.board[row][col] == 0

	def draw_figures(self):
		for row in range(BOARD_ROWS):
			for col in range(BOARD_COLS):
				if str(self.board[row][col]).find("p") != -1:
					num = int(self.board[row][col].replace("p_", ""))
					self.surface.blit(PLANTS[f"{num}"][0], ((col) * SQUARE_SIZE, (row - 1) * SQUARE_SIZE))


	def input(self):
		keys = pygame.key.get_pressed()
		mouse = pygame.mouse.get_pressed()
		current_time = pygame.time.get_ticks()

		if current_time - self.last_key_time > self.key_cooldown:
			if keys[pygame.K_RIGHT]:
				self.plantNum += 1
				if self.plantNum > len(PLANTS):
					self.plantNum = 1
				self.last_key_time = current_time
			elif keys[pygame.K_LEFT]:
				self.plantNum -= 1
				if self.plantNum < 1:
					self.plantNum = len(PLANTS)
				self.last_key_time = current_time

		if mouse[0]:
			pos = pygame.mouse.get_pos()
			mouseX = pos[0]
			mouseY = pos[1]

			clicked_row = mouseY // SQUARE_SIZE
			clicked_col = mouseX // SQUARE_SIZE

			if self.available_square(clicked_row, clicked_col):
				self.mark_square(clicked_row, clicked_col, f'p_{self.plantNum}')
				plant = Plant(((clicked_col) * SQUARE_SIZE, (clicked_row - 1) * SQUARE_SIZE), self.plantNum)
				self.all_plants.add(plant)

	def run(self):
		self.surface.fill('black')
		self.input()
		self.surface.blit(MAP_IMAGE, (0, 0))

		if len(self.all_plants) > 0:
			if self.timer.update():
				self.all_plants.update()
			self.all_plants.draw(self.surface)

		self.surface.blit(BLOCK, (0, 0))
		self.surface.blit(PLANTS[f"{self.plantNum}"][0], (10, 10))