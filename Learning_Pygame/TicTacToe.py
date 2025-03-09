import pygame
pygame.init()
screen = pygame.display.set_mode((1650, 825))
pygame.display.set_caption("Pygame Window")

image = pygame.image.load('map.png', "map").convert_alpha()
image = pygame.transform.scale(image, (1650, 825))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 255, 0))
    screen.blit(image, (0, 0))
    pygame.display.flip()
pygame.quit()