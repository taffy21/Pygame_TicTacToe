import pygame
from pygame.locals import *
import sys
import pygwidgets

class Screen:
    def __init__(self, window, image):
        self.window = window
        self.image = pygame.image.load(image)
        #self.image = pygame.transform.scale(self.image, (600, 800))
        self.rect = self.image.get_rect()

    def draw(self):
        self.window.blit(self.image, (0, 50))

# CONSTANTS
BLACK = (0, 0, 0)
FRAMPS = 30
WIDTH = 600
HEIGHT = 800

# INITIALISATIONS
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ophid")
clock = pygame.time.Clock()

# ASSETS

# VARIABLES
fin = Screen(window, r"C:\Users\Administrator.SGANDA-HP\Downloads\portal.png")
qn  = pygwidgets.DisplayText(window, (0, 0), "Where do you click to create a new Request?", textColor=(255,255,255), fontSize=24)
btn = pygwidgets.TextButton(window, (400, 0), "Click to Confirm Answer")

# LOOPS


 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEMOTION:
            pass

        if btn.handleEvent(event):
            print("Clicked")
    
    window.fill(BLACK)
    qn.draw()
    btn.draw()
    fin.draw()
    pygame.display.update()
    clock.tick(FRAMPS)


