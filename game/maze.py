# -*- coding: utf-8 -*-

import random

"""Creating a Labyrinthe's class to make
the maze"""


class Maze(list):
    """class to build a maze from a list of list"""
    def __init__(self, table):
        self.table = table

    def find_path_pos(self):
        """Method to find path position in the list"""
        path_position = []
        for y, line in enumerate(self.table, 1):
            for x, column in enumerate(line, 1):
                if column == 0 or column == 2:
                    volume = [x, y]
                    path_position.append(volume)
        return path_position

    def find_wall_pos(self):
        """Method to find wall position in the list"""
        wall_position = []
        for y, line in enumerate(self.table, 1):
            for x, column in enumerate(line, 1):
                if column == 1:
                    volume = [x, y]
                    wall_position.append(volume)
        return wall_position

    def find_guard_pos(self):
        """Method to find guard position in the list"""
        guard_position = []
        for y, line in enumerate(self.table, 1):
            for x, column in enumerate(line, 1):
                if column == 3:
                    volume = [x, y]
                    guard_position.append(volume)
        return guard_position

    def find_start_pos(self):
        """Method to find start position in the list"""
        for y, line in enumerate(self.table, 1):
            for x, column in enumerate(line, 1):
                if column == 2:
                    return [x, y]

    def rdm_object(self):
        """Method to choose a position for objects to be retrieved"""
        path = self.find_path_pos()
        rdm_pos = random.choice(path)
        return rdm_pos

    def check_path(self, position):
        """Method to control if a position is in the path of the maze"""
        if position in self.find_path_pos():
            return True
