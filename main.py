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
DISPLAY_WIDTH = 700
DISPLAY_HEIGHT = 500
FPS = 60

############################################################
############################################################

pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Forest Scene')

star_x = 50
starx_velo = 1
star_y = 50
stary_velo = 1
star_rad = 8

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    screen.fill(BLUE)

    # functions
    def trees(place, fill, x1, y1, mult):
        space = 180 * mult
        pygame.draw.polygon(place, fill, ((x1 + space, y1), (x1 - 50 + space, y1 + 150), (x1 - 25 + space, y1 + 130), (x1 - 60 + space, y1 + 250),
        (x1 - 35 + space, y1 + 230), (x1 - 100 + space, 700), (x1 + 100 + space, 700), (x1 + 25 + space, y1 + 230),
        (x1 + 50 + space, y1 + 250), (x1 + 15 + space, y1 + 130), (x1 + 40 + space, y1 + 150)))

    def stars(place, fill, x1, y1, width, mult = 0):
        space = 75 * mult
        pygame.draw.circle(place, fill, (x1 + space, y1), width)


    # drawing

    stars(screen, WHITE, star_x, star_y, star_rad)
    star_x += starx_velo
    star_y += stary_velo
    if star_x > DISPLAY_WIDTH or star_x < 0:
        starx_velo *= -1

    if star_y > DISPLAY_HEIGHT or star_y < 0:
        stary_velo *= -1


    # stars
    for multiplier in range(20):
        color = random.choice(STARS)
        stars(screen, color, -10, 130, 8, multiplier)
        stars(screen, color, 40, 70, 8, multiplier)
        stars(screen, color, 20, 10, 8, multiplier)


    # trees
    for multiplier in range (4):
        trees(screen, GREEN, 100, 100, multiplier)
        trees(screen, GREEN2, 20, 100, multiplier)


pygame.quit()
