import pygame

from setting import *

class Plant(pygame.sprite.Sprite):
    def __init__(self, pos, index):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.images = PLANTS[f"{index}"]
        self.maxFrames = len(self.images)
        self.frame = 0
        self.rect = pos
        self.image = self.images[self.frame]

    def update(self):
        if self.frame < self.maxFrames - 1:
            self.frame += 1
        self.image = self.images[self.frame]
