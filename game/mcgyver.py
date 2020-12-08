# -*- coding: utf-8 -*-


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

    def self_position(self):
        """Method to return MacGyver position"""
        return self.position
