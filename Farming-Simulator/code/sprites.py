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

        self.already = 5

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
        
    def auto_collect(self):
        if self.already <= 0:
            if self.is_harvest():
                self.harvest_time()
                self.already = 5
                return (self.harvestPrice, self.life)
        return (0, self.life)

class Box(pygame.sprite.Sprite):
    def __init__(self, groups, pos, size, color):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)

    def set_center(self, center):
        self.rect.center = center

    def update(self, increase):
        self.rect.top += increase

    def add_text(self, text, font, color, pos = None):
        self.image.fill(self.color)
        text_surface = font.render(text, True, color)
        if pos is None:
            text_rect = text_surface.get_rect(center=(self.rect.center[0] - self.rect.topleft[0], self.rect.center[1] - self.rect.topleft[1]))
        else:
            text_rect = text_surface.get_rect(topleft=pos)
        self.image.blit(text_surface, text_rect)

        



class Container(pygame.sprite.Sprite):
    def __init__(self, groups, pos, size, colour):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.colour = colour
        self.rect = self.image.get_rect(topleft=pos)
        self.group = pygame.sprite.Group()
        self.next_child_y = 0
        self.lenght = 0
    
    def set_center(self, center):
        self.rect.center = center

    def create_child(self, size, color):
        child_pos = (0, self.next_child_y)
        box = Box(self.group, child_pos, size, color)
        self.lenght += size[1]
        self.next_child_y += size[1]
        return box 

    def create_with_text(self, size, color, text, font, fontColour, pos = None):
        box = self.create_child(size, color)
        box.add_text(text, font, fontColour, pos)
        return box

    def update(self):
        self.image.fill(self.colour)
        self.group.draw(self.image)

    def move(self, increase):
        if (increase < 0 and self.next_child_y + increase > self.image.get_height()) or (increase > 0 and self.next_child_y < self.lenght) :
            self.next_child_y += increase
            self.group.update(increase)

    def close(self):
        self.group.empty()
        self.kill()
