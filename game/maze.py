# -*- coding: utf-8 -*-
 
import random

class Maze(list):
    def __init__(self, table):
        self.table = table
        
    def find_path_pos(self):
        path_position = []
        for y, line in enumerate(self.table, 1):
            for x, column in enumerate(line, 1):
                if column == 0 or column == 2:
                    volume = [x, y]
                    path_position.append(volume)
        return path_position

    def find_wall_pos(self):
        wall_position = []
        for y, line in enumerate(self.table, 1):
            for x, column in enumerate(line, 1):
                if column == 1:
                    volume = [x, y]
                    wall_position.append(volume)
        return wall_position

    def find_guard_pos(self):
        guard_position = []
        for y, line in enumerate(self.table, 1):
            for x, column in enumerate(line, 1):
                if column == 3:
                    volume = [x, y]
                    guard_position.append(volume)
        return guard_position    

    def find_start_pos(self):
        for y, line in enumerate(self.table, 1):
            for x, column in enumerate(line, 1):
                if column == 2:
                    return [x, y]

    def rdm_object(self):
        path = self.find_path_pos()
        rdm_pos = random.choice(path)
        return rdm_pos
            
    def check_path(self, position):
        if position in self.find_path_pos():
            return True
                
