import pygame

class SpriteSheet():
    def __init__(self, path):
        pygame.display.init()
        pygame.display.set_mode((1, 1), pygame.NOFRAME)  # Create a minimal display
        self.sheet = pygame.image.load(path)

    def get_image(self, pos, frame, size, scale , leftToRight = True, colour = None):
        image = pygame.Surface((size[0], size[1])).convert_alpha()
        image.fill((0, 0, 0, 0))  # Fill with transparent pixels

        if leftToRight:
            image.blit(self.sheet, (0, 0), (pos[0] + (frame * size[0]), pos[1], size[0], size[1]))

        image = pygame.transform.scale(image, (size[0] * scale, size[1] * scale))

        if colour is not None :
            image.set_colorkey(colour)

        return image
    
    def get_images_sheet(self, pos, size, frames, scale, leftToRight = True, colour = None):
        images = []
        for i in range(frames):
            if not frames == 0:
                images.append(self.get_image( pos, i, size, scale, leftToRight, colour))

        return images
    
    # data
    # {
    #     "type": {
    #         "pos": [x, y],
    #         "size": [w, h],
    #         "frames": n
    #     }
    # }
    
    def get_all_sprites(self, data, size, scale):
        imagesData = {}
        for typeSprite in data.keys():
                imagesData[typeSprite] = self.get_images_sheet(data[typeSprite]["pos"], size, data[typeSprite]["frame"]-1, scale)
        
        return imagesData

