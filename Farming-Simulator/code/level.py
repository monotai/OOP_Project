import pygame
from settings import *
from sprite import Generic


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.all_sprites = CameraGroup()

        self.setup()

    def setup(self):
        Generic(pos = (0, 0),
                surf = pygame.image.load('../graphics/map.png').convert_alpha(),
                groups = self.all_sprites,
                z = LAYERS['ground'])

    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.custom_draw()
        self.all_sprites.update(dt)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.displaySurface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
    
    def custom_draw(self):

        

        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    self.displaySurface.blit(sprite.image, sprite.rect)