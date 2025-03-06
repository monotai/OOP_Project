import pygame

class SpriteSheet():
    def __init__(self, path):
        pygame.display.init()
        pygame.display.set_mode((1, 1), pygame.NOFRAME)  # Create a minimal display
        self.sheet = pygame.image.load(path)
    
    def get_image(self, pos_2, size_2, scale_2, colour = None):
            image = pygame.Surface(size_2).convert_alpha()
            image.fill((0, 0, 0, 0))

            image.blit(self.sheet, (0, 0), (pos_2[0], pos_2[1], size_2[0], size_2[1]))
            image = pygame.transform.scale(image, scale_2)

            if colour is not None:
                image.set_colorkey(colour)

            return image

    def get_images_sheet(self, pos_2, frames_2, size_2, scale_2, colour = None):
        images = []
        for i in range(frames_2[0]):
            for j in range(frames_2[1]):
                images.append(self.get_image((pos_2[0] + i * size_2[0], pos_2[1] + j * size_2[1]), size_2, scale_2, colour))

        return images
    
    # data
    # {
    #     "type": {
    #         "pos": [x, y],
    #         "size": [w, h],
    #         "frames": [m, n]
    #     }
    # }
    # image is an rangtangle
    
    def get_all_sprites(self, data, scale_2, size_2 = None):
        imagesData = {}
        
        if size_2 is None:
            for typeSprite in data.keys():
                imagesData[typeSprite] = self.get_images_sheet(data[typeSprite]["pos"], data[typeSprite]["frames"], data[typeSprite]["size"], scale_2)
        else :
            for typeSprite in data.keys():
                imagesData[typeSprite] = self.get_images_sheet(data[typeSprite]["pos"], data[typeSprite]["frames"], size_2, scale_2)

        return imagesData
    
