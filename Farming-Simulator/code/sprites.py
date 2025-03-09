import pygame

from setting import *

class Plant(pygame.sprite.Sprite):
    def __init__(self, pos, key, frame):
        pygame.sprite.Sprite.__init__(self)
        self.key = key
        self.pos = pos
        self.images = PLANTS[key]
        self.maxFrames = len(self.images)
        self.frame = frame
        self.rect = self.images[self.frame].get_rect(topleft=pos)
        self.image = self.images[self.frame]
        self.daysInPhase = PLANTS_DATA[key]["DaysInPhase"]
        self.reGrow = PLANTS_DATA[key]["RegrowDays"]
        self.addColor = PLANTS_DATA[key]["TintColors"]
        self.harvestPrice = PLANTS_DATA[key]["HarvestPrice"]
        self.isGrow = False
        self.phase = 0
        self.frameHarvest = self.maxFrames - 1
        self.life = 1
        if self.reGrow > 0:
            self.life = 3
            self.frameHarvest -= 1
        if len(self.addColor) > 0:
            self.frameHarvest -= 1

        

    def update(self):
        self.phase += 1
        
        if self.frame < self.frameHarvest:
            if self.phase >= self.daysInPhase[self.frame - 1]:
                self.isGrow = True
                self.phase = 0
            else: self.isGrow = False
        elif self.frame == self.frameHarvest:
            self.phase = 0
            self.isGrow = False
            
        else:
            self.isGrow = False
            if self.phase == self.reGrow:
                self.frame -= 1
                self.phase = 0

        if self.isGrow and self.frame < self.maxFrames - 1:
            self.frame += 1
        self.image = self.images[self.frame]

    def is_harvest(self):
        return True if (self.frame == self.frameHarvest) else False
    
    def harvest_time(self):
        self.life -= 1
        if self.life == 0:
            self.kill()
            return False
        else:
            self.frame += 1
            self.image = self.images[self.frame]
            return True
