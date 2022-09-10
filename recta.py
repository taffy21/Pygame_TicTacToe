import pygame
from pygame.locals import *
import pygwidgets

class Rectangle:
    """initiates an instance of a rectangle"""
    played = "no"
    clear = "yes"
    def __init__(self, window,loc, x, y):
        self.window = window
        self.loc = loc
        self.x = x
        self.y = y
        self.surf = pygame.Surface((self.x, self.y))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(topleft = self.loc)     
    
    def draw(self):
        self.window.blit(self.surf, self.loc)

    def drawEx(self):
        pygame.font.init()
        letter = pygame.font.SysFont(None,230)
        letter = letter.render("X", False, (0, 0, 0))
        self.surf.blit(letter, (0, 0))        
    
    def drawOh(self):
        pygame.font.init()
        letter = pygame.font.SysFont(None,230)
        letter = letter.render("O", False, (0, 0, 0))
        self.surf.blit(letter, (0, 0))


    
    
