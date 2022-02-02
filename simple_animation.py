# Simple Animation with PyGame, Jahaun Gilmore, 2/2/22, 2:26PM, v0.1

import pygame, sys, time
from pygame.locals import *

# Setup PyGame
pygame.init()

# Setup the Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode(WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!') 