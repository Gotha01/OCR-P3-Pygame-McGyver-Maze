# -*- coding: utf-8 -*-

import os.path
import pygame

pygame.init()


#Game's Structure
image_start = pygame.image.load("ressources/images/imgstart.jpg")
image_start.convert

red = (255, 0, 0)
title_menu_font = pygame.font.Font("ressources/fonts/Geddes_bold.otf", 35)
title_menu_text = title_menu_font.render("THE GAME", True, red)
ctp_font = pygame.font.Font("ressources/fonts/Geddes_bold.otf", 20)
click_to_play = ctp_font.render("Click any key to start the game", True, red)
window_resolution = (520, 520)
black = (0,0,0)




#Table of the level:

tab_width = tab_height = 15
font_wall = pygame.image.load("ressources/images/wall_font_30_30.png")
font_path = pygame.image.load("ressources/images/floor_font_30_30.png")
font_start = pygame.image.load("ressources/images/start.png")
font_guard = pygame.image.load("ressources/images/Guardian.png")


level_disposition = [
[1,1,0,1,1,1,0,0,0,0,0,0,0,1,1],
[2,1,0,0,0,1,1,0,1,1,1,1,0,1,0],
[0,1,0,1,0,0,0,0,1,0,0,1,0,1,0],
[0,1,0,1,0,1,1,1,1,1,0,1,0,1,0],
[0,1,1,1,0,1,0,1,0,1,0,1,0,1,0],
[0,0,0,0,0,1,0,1,0,1,0,1,0,1,0],
[0,1,0,1,1,1,0,1,0,1,0,0,0,0,0],
[0,1,0,1,0,0,0,1,0,1,0,1,1,1,1],
[1,1,0,0,0,1,0,1,0,1,0,0,0,0,0],
[0,1,1,1,1,1,0,1,0,1,0,1,1,1,0],
[0,0,0,0,0,0,0,1,0,1,0,1,0,1,3],
[0,1,0,1,1,1,1,1,0,1,1,1,0,1,1],
[0,1,0,0,0,0,0,1,0,0,0,1,0,0,0],
[1,1,1,0,1,0,1,1,0,1,0,1,1,1,0],
[0,0,0,0,1,0,0,0,0,1,0,0,0,0,0]]

line_len = len(level_disposition)
column_len = len(level_disposition[0])

class Structure(list):
    def __init__(self, table, surface):
        self_table = table
        self_surface = surface

    def draw_structure(self, table, surface):   
        table_x = table_y = 30 
        for column in table:
            for i in column:
                if i == 0:
                    surface.blit(font_path, [table_x, table_y])
                    table_x += 30
                elif i == 1:
                    surface.blit(font_wall, [table_x, table_y])
                    table_x += 30
                elif i == 2:
                    surface.blit(font_start, [table_x, table_y])
                    table_x += 30
                elif i == 3:
                    surface.blit(font_guard, [table_x, table_y])
                    table_x += 30
            table_y += 30
            table_x = 30    
            pygame.display.flip()
        
"""
class Mac_gyver(self, move, health, objects):
"""