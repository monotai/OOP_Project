# pygame and sys

```
import pygame
import sys

pygame.init()
pygame.display.set_mode((SCREEN_WITHD, SCREEN_HIEGHT))
pygame.display.set_caption('CAPTION')

pygame.display.update()

pygame.quit()
sys.exit()
```

## Time

```
clock = pygame.time.Clock()
dt = clock.tick() / 1000
```

## Event

```
for event in pygame.event.get():
	if event.type == pygame.QUIT:
		pygame.quit()
		sys.exit()
	elif event.type == pygame.K_k:
		print('Button K is touch')
	elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y
```

# Run In File main

```
if __name__ == '__main__'
```

## Surface

```
pygame.diplay.get_surface()
```

## sprite.Group

```
block = pygame.sprite.Group()
block.sprites()
for block in blocks:
	block.rect
```

## sprite.Sprite

```
pygame.sprite.Sprite

```

## Vector

```
pygame.math.Vector2()
```

## Set to Surface

```
rect = (X, Y)
surf = pygame.image.load(PATH).convert_alpha()
surf = pygame.tranfrom.scale(surf, (WITH, HIEGHT))
image = surf
pygame.display.get_surface().blit(image, rect)

pygame.display.update() # if you wante to display imediatly
```

## Rect

```
rect = pygame.Rect(X, Y, WIDTH, HIEGHT)
rect.collidepoint(POINT)
```

## Sound

```
sound = pygame.mixer.Sound(PATH)
sound.set_valume(VALUE)
```

# enumerate

```
emumerate(DATA)
```
