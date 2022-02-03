# Simple Animation with PyGame, Jahaun Gilmore, 2/3/22, 6:56PM, v0.4

import pygame, sys, time
from pygame.locals import *

# Setup PyGame
pygame.init()

# Setup the Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode(WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!') 

# Setup the direction variables.
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

# Setup color values
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Setup the box data
b1 = ('rect':pygame.Rect(300, 50, 80, 100), 'color':RED, 'dir':UPRIGHT)
b2 = ('rect':pygame.Rect(200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT)
b3 = ('rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNRIGHT)
boxes = [b1, b2, b3]