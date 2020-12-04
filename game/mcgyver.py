# -*- coding: utf-8 -*-

import pygame


class Mcgyver:
    def __init__(self, position):
        """Initialize the character and his position"""
        self.position = position
        self.inventory = 0

    def move(self, direction):
        if direction == "u":
            self.position[1] -= 1
            return self.position
        elif direction == "d":
            self.position[1] += 1
            return self.position
        elif direction == "l":
            self.position[0] -= 1
            return self.position
        elif direction == "r":
            self.position[0] += 1
            return self.position
    
    def check_item_pos(self):
        item = 0
        if self.position == item_pos:
            item +=1
            return item


    def self_position(self):
        return self.position

    def show_health(self):
        pass
    