# go to terminal (@ bottom of screen) and write "pip install pygame" after PS C: line
import pygame
import math
import random

# color constants
BLUE = (7, 71, 92)
GREEN = (6, 69, 22)
GREEN2 = (22, 87, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 220, 71)
STARS = [WHITE, YELLOW]

# math constants

# game constants
SIZE = (700, 500)
FPS = 60

############################################################
############################################################

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Forest Scene')

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLUE)


    # functions
    def trees(place, color, x1, y1, mult):
        space = 180 * mult
        tree = pygame.draw.polygon(place, color, ((x1 + space, y1), (x1 - 50 + space, y1 + 150), (x1 - 25 + space, y1 + 130), (x1 - 60 + space, y1 + 250),
        (x1 - 35 + space, y1 + 230), (x1 - 100 + space, 700), (x1 + 100 + space, 700), (x1 + 25 + space, y1 + 230),
        (x1 + 50 + space, y1 + 250), (x1 + 15 + space, y1 + 130), (x1 + 40 + space, y1 + 150)))


    # drawing
    # stars
    for multiplier in range(20):
        color = random.choice(STARS)
        num = random.randint(10, 20)
        pygame.draw.circle(screen, color, (-10 + 75 * multiplier, 130), 8)
        pygame.draw.circle(screen, color, (40 + 75 * multiplier, 70), 8)
        pygame.draw.circle(screen, color, (20 + 75 * multiplier, 10), 8)

    # trees
    for multiplier in range (4):
        trees(screen, GREEN, 100, 100, multiplier)
        trees(screen, GREEN2, 20, 100, multiplier)

    pygame.display.flip()

pygame.quit()
