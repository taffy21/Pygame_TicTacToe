import pygame
import sys
from pygame.locals import *


class Word:
    def __init__(self, text):
        pygame.font.init()
        self.text = text        
        self.typeset = pygame.font.SysFont(size=30)
        self

# CONSTATNS
BLACK = (50, 50, 50)
WHITE = (255, 255, 255)
FRAMPS = 30
WIDTH = 400
HEIGHT = 400

# INIT
pygame.init()
window = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("Try.exe")
clock = pygame.time.Clock()

# ASSETS

# VARIABLES


# LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    window.fill(BLACK)

    pygame.display.update()

    clock.tick(FRAMPS)