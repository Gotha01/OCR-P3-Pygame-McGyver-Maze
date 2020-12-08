# -*- coding: utf-8 -*-

import pygame

import game.level_table as lvl
import game.visual as vis
import game.maze as cmaz
import game.mcgyver as mac

"""Module to import all the classes
and making them work together"""

pygame.init()


class Accessor:
    """Class to manage the operations of the game"""
    def __init__(self):
        self.inventory = 0
        self.launched = bool
        self.endgame_pos = [15, 10]
        self.maze = cmaz.Maze(lvl.level_disposition)
        self.mac_gyver = mac.Mcgyver(self.maze.find_start_pos())
        self.vis = vis.Visual()
        self.vis.loading_page()
        self.loading_loop()
        self.vis.game_page()
        self.structure_making()
        self.objects_pos = self.objects_making()
        self.mac_gyver_making()
        self.game_loop()
        self.endgame_loop()

    def loading_loop(self):
        """Loading page loop before running the game"""
        loading = True
        while loading:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    loading = False

    def game_loop(self):
        """Game loop to run the game"""
        self.launched = True
        while self.launched:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    pos_x = self.mac_gyver.position[0]
                    pos_y = self.mac_gyver.position[1]
                    if event.key == pygame.K_UP:
                        self.mac_gyver_move("u", "d", pos_x, pos_y)
                    elif event.key == pygame.K_DOWN:
                        self.mac_gyver_move("d", "u", pos_x, pos_y)
                    elif event.key == pygame.K_LEFT:
                        self.mac_gyver_move("l", "r", pos_x, pos_y)
                    elif event.key == pygame.K_RIGHT:
                        self.mac_gyver_move("r", "l", pos_x, pos_y)

    def endgame_loop(self):
        """Loop to show end of game"""
        endgame = True
        while endgame:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                    endgame = False

    def structure_making(self):
        """Method to generate a 2D maze"""
        path = self.maze.find_path_pos()
        for element in path:
            self.vis.draw_path(element[0], element[1])
        wall = self.maze.find_wall_pos()
        for element in wall:
            self.vis.draw_wall(element[0], element[1])
        guard = self.maze.find_guard_pos()
        for element in guard:
            self.vis.draw_guard(element[0], element[1])

    def objects_making(self):
        """Method to generate three random position objects"""
        obj_created = False
        needle_pos = self.maze.rdm_object()
        tube_pos = self.maze.rdm_object()
        ether_pos = self.maze.rdm_object()
        while obj_created is False:
            self.vis.draw_needle(needle_pos[0], needle_pos[1])
            if tube_pos != needle_pos:
                self.vis.draw_tube(tube_pos[0], tube_pos[1])
                if ether_pos != tube_pos:
                    self.vis.draw_ether(ether_pos[0], ether_pos[1])
                    obj_created = True
        return [needle_pos, tube_pos, ether_pos]

    def mac_gyver_making(self):
        """Method to generate MacGyver"""
        pos_x = self.maze.find_start_pos()[0]
        pos_y = self.maze.find_start_pos()[1]
        self.vis.draw_macgyver(pos_x, pos_y)

    def mac_gyver_move(self, direction, _direction, x, y):
        """Method to make MacGyver move"""
        new_position = self.mac_gyver.move(direction)
        if self.maze.check_path(new_position):
            if new_position in self.objects_pos:
                self.inventory += 1
                self.objects_pos.remove(new_position)
            self.vis.advance_mac(x, y, new_position)
            if new_position == self.endgame_pos:
                self.finish()
        else:
            self.mac_gyver.move(_direction)
            self.vis.draw_macgyver(x, y)

    def finish(self):
        """Method to define if the player has won or not"""
        self.launched = False
        if self.inventory == 3:
            self.vis.victory_page()
        else:
            self.vis.lose_page()
