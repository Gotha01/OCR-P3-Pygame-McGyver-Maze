# -*- coding: utf-8 -*-

import os
import time
from pprint import pprint

import pygame
from pygame.locals import *

import settings

pygame.init()

loading = True
launched = True


while loading:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loading = False 
    
    #Page de démarrage
    
    pygame.display.set_caption("Mac Gyver Survivor")
    window_surface = pygame.display.set_mode(settings.window_resolution)
    window_surface.fill(settings.black)
    window_surface.blit(settings.image_start, [15, (int(settings.window_resolution[1]) - int(settings.image_start.get_height() ) ) / 2 + 10])
    window_surface.blit(settings.title_menu_text, [180 , 30])
    window_surface.blit(settings.click_to_play, [130, 460])
    pygame.display.flip()
    

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            loading = False

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    
    pygame.display.set_caption("Mac Gyver Survivor")
    window_surface = pygame.display.set_mode(settings.window_resolution)
    window_surface.fill(settings.black)
    Maze = settings.Structure(settings.level_disposition, window_surface)
    Maze.draw_structure(settings.level_disposition, window_surface)
