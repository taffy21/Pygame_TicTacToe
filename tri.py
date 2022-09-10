import pygame
import sys
import recta
import pygwidgets

# CLASS


# FUNCTIONS
def tilePressed(tile_list, arg2): 
    for tile in tile_list:
        if tile.rect.collidepoint(arg2):            
            tile.played = "yes"

# CONSTANTS
BLACK = (30, 30, 30)
RED = (255, 0, 0)
SIZE = 600
FRMS = 30

# INITIALISATIONS
pygame.init()
window = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("game")
clock = pygame.time.Clock()

# ASSETS

# VARIABLES
tile = recta.Rectangle(window, (0,0), 200, 200)
tile2 = recta.Rectangle(window, (200, 0), 200, 200)
btn = pygwidgets.TextButton(window, (280, 500), "Restart")

text_x = pygwidgets.DisplayText(window, (0, 0), "X", fontSize=230)
status = "UNPLAYED"

# LOOPS
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if tile.rect.collidepoint(event.pos):
                status = "PLAYED"
                
        if btn.handleEvent(event):
            status = "UNPLAYED"
            
    window.fill((255, 0, 0))
    
    if status == "UNPLAYED":        
        tile.draw()
        btn.draw()
        window.fill((255, 0, 0))
    if status == "PLAYED":
        tile.draw()
        pygwidgets.DisplayText(tile.surf, (0, 0), "X", fontSize=230).draw()
        #tile.drawEx()
        btn.draw()    
        
    pygame.display.update()

    clock.tick(FRMS)

