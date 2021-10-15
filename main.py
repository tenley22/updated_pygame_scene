# go to terminal (@ bottom of screen) and write "pip install pygame" after PS C: line
import pygame
import math
import random

# color constants
BLUE = (7, 71, 92)
GREEN = (6, 69, 22)
GREEN2 = (22, 87, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 221, 71)
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
starx_velo = 2
star_y = 50
stary_velo = 2
star_side = 40


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    if star_x + star_side > DISPLAY_WIDTH or star_x < 0:
        starx_velo *= -1

    if star_y + star_side > 200 or star_y < 0:
        stary_velo *= -1
  



    screen.fill(BLUE)

    # drawing
    #star
    
    color = random.choice(STARS)
    pygame.draw.polygon(screen, color, ((star_x, star_y), (star_x-5, star_y-20), (star_x-30, star_y-30), (star_x-5, star_y-40), (star_x, star_y-70), (star_x+5, star_y-40), (star_x+30, star_y-30), (star_x+5, star_y-20)))
    star_x += starx_velo
    star_y += stary_velo
  


    # stars original 
    '''
    for multiplier in range(20):
        color = random.choice(STARS)
        num = random.randint(10, 20)
        pygame.draw.circle(screen, color, (-10 + 75 * multiplier, 130), 8)
        pygame.draw.circle(screen, color, (40 + 75 * multiplier, 70), 8)
        pygame.draw.circle(screen, color, (20 + 75 * multiplier, 10), 8)
    '''

    # trees
    for multiplier in range (4):
        pygame.draw.polygon(screen, GREEN, ((100 + 180*multiplier, 100), (50 + 180*multiplier, 250), (75 + 180*multiplier, 230), (40 + 180*multiplier, 350), (65 + 180*multiplier, 330), (0 + 180*multiplier, 700), (200 + 180*multiplier, 700), (125 + 180*multiplier, 330), (150 + 180*multiplier, 350), (115 + 180*multiplier, 230), (140 + 180*multiplier, 250)))

        pygame.draw.polygon(screen, GREEN2, ((20 + 180 * multiplier, 100), (-40 + 180 * multiplier, 250), (-15 + 180 * multiplier, 230), (-50 + 180 * multiplier, 350), (-25 + 180 * multiplier, 330), (-80 + 180 * multiplier, 700), (120 + 180 * multiplier, 700), (35 + 180 * multiplier, 330), (60 + 180 * multiplier, 350), (25 + 180 * multiplier, 230), (50 + 180 * multiplier, 250)))




    pygame.display.flip()

pygame.quit()
