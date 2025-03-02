import pygame, sys
from settings import *
from level import *

class Game: # our class for game running
	def __init__(self):
		pygame.init() # initaily
		self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # screen size
		pygame.display.set_caption('Farming Simulator') # caption
		self.clock = pygame.time.Clock() # clock
		self.level = Level()

	def run(self): # run game
		while True: # loop
			for event in pygame.event.get(): # get event on sceen
				if event.type == pygame.QUIT: # click on quit button
					pygame.quit() # quit game
					sys.exit() # stop program
  
			dt = self.clock.tick() / 1000 # fram rate
			self.level.run(dt)
			pygame.display.update() # diplay changing like move, ...

if __name__ == '__main__': # first running ?
	game = Game() # defind instand
	game.run() # run game