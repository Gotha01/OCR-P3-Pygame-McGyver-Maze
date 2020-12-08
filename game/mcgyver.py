# -*- coding: utf-8 -*-

import pygame


class Mcgyver:
    def __init__(self, position):
        """Initialize MacGyver and his position"""
        self.position = position
        self.inventory = 0

    def move(self, direction):
        """Method to attribuate a new position to MacGyver"""
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
        """Method to check if MacGyver is on an object position"""
        item = 0
        if self.position == item_pos:
            item +=1
            return item

    def self_position(self):
        """Method to return MacGyver position"""
        return self.position
    