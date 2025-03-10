import pygame
import sys

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Box dimensions
BOX_WIDTH, BOX_HEIGHT = 100, 50
EXPANDED_BOX_HEIGHT = 150

# Colors
BACKGROUND_COLOR = (30, 30, 30)
BOX_COLOR = (70, 130, 180)
EXPANDED_BOX_COLOR = (255, 99, 71)

# Scroll speed
SCROLL_SPEED = 5

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Scrollable Boxes with Expandable Feature")
clock = pygame.time.Clock()

class Box(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.original_height = height
        self.expanded = False

    def update(self, *args):
        if self.expanded:
            self.image = pygame.Surface((self.rect.width, EXPANDED_BOX_HEIGHT))
            self.image.fill(EXPANDED_BOX_COLOR)
            self.rect.height = EXPANDED_BOX_HEIGHT
        else:
            self.image = pygame.Surface((self.rect.width, self.original_height))
            self.image.fill(BOX_COLOR)
            self.rect.height = self.original_height

boxes = pygame.sprite.Group()
padding = 10
for i in range(20):  # Create 20 boxes
    x = padding
    y = i * (BOX_HEIGHT + padding) + padding
    box = Box(x, y, BOX_WIDTH, BOX_HEIGHT, BOX_COLOR)
    boxes.add(box)

running = True
scroll_offset = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                for box in boxes:
                    if box.rect.collidepoint(event.pos[0], event.pos[1] + scroll_offset):
                        box.expanded = not box.expanded

    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        scroll_offset = max(scroll_offset - SCROLL_SPEED, 0)
    if keys[pygame.K_DOWN]:
        scroll_offset += SCROLL_SPEED

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw only visible boxes
    for box in boxes:
        box.rect.y -= scroll_offset
        if box.rect.colliderect(screen.get_rect()):
            screen.blit(box.image, box.rect)
        box.rect.y += scroll_offset

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
