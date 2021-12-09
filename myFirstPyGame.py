# My First Game, Jahaun Gilmore, 12/9/21 2:27pm, v0.6

import pygame, sys
from pygame.locals import *

# Start PyGame
pygame.init()

# Setup our window.
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Hello World")

# Setup Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Setup font.
basicFont = pygame.font.SysFont(None, 48)

# Setup text.
text = basicFont.render('Hello, World!', True, WHITE, BLUE)
textRect = text.get_rect() 
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Fill background color
windowSurface.fill(WHITE)

# Draw a polygon onto the screen.
pygame.draw.polygon(windowSurface, BLUE, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

#Draw a polygon onto the screen.
pygame.draw.line(windowsSurface, GREEN, (60,60), (120,60), 4)
pygame.draw.line(windowsSurface, BLUE, (256,300), (300,400), 3)
pygame.draw.line(windowsSurface, NOTRED, (100,200), (140,235), 2)