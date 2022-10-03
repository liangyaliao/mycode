#TODO
# Create the Screen.
# Create the Snake.
# Moving the Snake.
# Game Over when Snake hits the boundaries.
# Adding the Food.
# Increasing the Length of the Snake.
# Displaying the Score.



import pygame
from pygame.locals import *
import time
import random
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'
#os.environ["SDL_VIDEODRIVER"] = "dummy"
#os.environ['SDL_VIDEODRIVER']='windlib'
#os.environ["SDL_VIDEODRIVER"] = "directfb"
pygame.init()
pygame.font.init()
pygame. display. set_mode(1000,1000)
pygame.display.list_modes()
WINDOW = 1000
screen = pygame.display.set_mode([WINDOW] * 2)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        screen.fill('black')       
        pygame.display.flip()
        clock.tick(60)

exit()      