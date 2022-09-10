import pygame
from pygame.locals import *
import sys
import pygwidgets
import recta
import time

# FUNCTIONS
def tilePressed(tile_list, arg2): 
    for tile in tile_list:
        if tile.rect.collidepoint(arg2):            
            tile.played = "yes"

def final_result(result):
    global start_screen, count
    
    if result[tile1] == result[tile2] == result[tile3] and result[tile1] != "":        
        start_screen = 'END'
        end_text.setValue(f"{result[tile1]}is the winner")
    elif result[tile4] == result[tile5] == result[tile6] and result[tile4] != "":
        start_screen = 'END'
        end_text.setValue(f"{result[tile4]} is the winner")
    elif result[tile7] == result[tile8] == result[tile9] and result[tile7] !="":
        start_screen = 'END'
        end_text.setValue(f"{result[tile7]} is the winner")
    elif result[tile1] == result[tile4] == result[tile7] and result[tile1] != "":
        start_screen = 'END'
        end_text.setValue(f"{result[tile1]} is the winner")
    elif result[tile2] == result[tile5] == result[tile8] and result[tile2] != "":
        start_screen = 'END'
        end_text.setValue(f"{result[tile2]} is the winner")
    elif result[tile3] == result[tile6] == result[tile9] and result[tile3] != "":
        start_screen = 'END'
        end_text.setValue(f"{result[tile3]} is the winner")
    elif result[tile1] == result[tile5] == result[tile9] and result[tile1] != "":
        start_screen = 'END'
        end_text.setValue(f"{result[tile1]} is the winner")
    elif result[tile3] == result[tile5] == result[tile7] and result[tile3] !="":
        start_screen = 'END'
        end_text.setValue(f"{result[tile3]} is the winner")
    elif count == 9:
        start_screen = "END"
        end_text.setValue(f"Draw - draw")

   
# CONSTANTS
BLACK = (50, 50, 50)
WHITE = (255, 255, 255)
RED = (255, 140, 59)
WIDTH = 400
HEIGHT = 400
FRMS = 30

# INITIALISATIONS
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()

# ASSETS

# VARIABLES
tile_size = 133.3
tile1 = recta.Rectangle(window, (0, 0), tile_size, tile_size)
tile2 = recta.Rectangle(window, (134, 0), tile_size, tile_size)
tile3 = recta.Rectangle(window, (268, 0), tile_size, tile_size)
tile4 = recta.Rectangle(window, (0, 134), tile_size, tile_size)
tile5 = recta.Rectangle(window, (134, 134), tile_size, tile_size)
tile6 = recta.Rectangle(window, (268, 134), tile_size, tile_size)
tile7 = recta.Rectangle(window, (0, 268), tile_size, tile_size)
tile8 = recta.Rectangle(window, (134, 268), tile_size, tile_size)
tile9 = recta.Rectangle(window, (268, 268), tile_size, tile_size)

tiles = [tile1, tile2, tile3, 
        tile4, tile5, tile6,
        tile7, tile8, tile9]

# START MENU
start_screen = "START"
start_btn  = pygwidgets.TextButton(window, (134, 268), "START")
display_txt = pygwidgets.DisplayText(window, (60, 100), "Welcome to Tic-Tac-Toe", textColor=WHITE, fontSize=36)

# TURNS
turn = "second"

# RESULT
result = {tile1:"", tile2:"", tile3:"",
         tile4:"", tile5:"", tile6:"",
         tile7:"", tile8:"", tile9:""}

# END SCREEN
end_btn = pygwidgets.TextButton(window, (134, 268), "RESTART")
end_text = pygwidgets.DisplayText(window, (60, 100), "", textColor=WHITE, fontSize=36)


count = 0

# LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()     
        
        if start_btn.handleEvent(event):
            start_screen = "PLAYING"      
             
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_screen == 'PLAYING':
                block_pressed = event.pos
                tilePressed(tiles, block_pressed) 
                                
                if turn == "first":
                    turn = "second"
                else:
                    turn = "first" 

        if end_btn.handleEvent(event):
            for i in result:
                result[i] = ""   
            for tile in tiles:
                tile.played = 'no'
                tile.clear = 'yes'   
                tile.surf.fill(RED) 
            turn = 'second'
            count = 0
                             
    if start_screen == "START":
        window.fill(BLACK)
        display_txt.draw()
        start_btn.draw()    
        
    if start_screen == "PLAYING":
        window.fill(BLACK)
        
        for tile in tiles:
            tile.draw()                
            
            if tile.played == 'yes' and tile.clear == 'yes':
                count+=1
                if turn == "first":
                    tile.drawEx()                    
                    tile.clear = 'no'
                    result[tile] = 'X'
                elif turn == "second": 
                    tile.drawOh()  
                    tile.clear = 'no'
                    result[tile] = 'O'
                                
            final_result(result)
            

    if start_screen == "END":
        window.fill(BLACK)
        end_text.draw()
        end_btn.draw()
              
    
    pygame.display.update()
    clock.tick(FRMS)

