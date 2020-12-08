import pygame

import game.constants as cst

pygame.init()


class Visual:
    """Class to to create the 2D version of the maze"""
    def __init__(self):
        # Game's Structure
        self.image_start = pygame.image.load(cst.LOAD)
        self.tmt_font = pygame.font.Font(cst.Bold_text_font, 35)
        self.title_menu_text = self.tmt_font.render(cst.TMT, True, cst.BL)
        self.ctp_font = pygame.font.Font(cst.Bold_text_font, 20)
        self.click_to_play = self.ctp_font.render(cst.CTP, True, cst.BL)
        self.inv_font = pygame.font.Font(cst.Bold_text_font, 20)
        self.inventory = self.inv_font.render(cst.INVENTORY, True, cst.BL)
        self.window_resolution = (520, 500)
        self.surface = pygame.display.set_mode(self.window_resolution)
        self.black = cst.BLACK
        self.vic_font_1 = pygame.font.Font(cst.Bold_text_font, 55)
        self.vic_text_1 = self.vic_font_1.render(cst.VICTORY_1, True, cst.BL)
        self.vic_font_2 = pygame.font.Font(cst.Bold_text_font, 30)
        self.vic_text_2 = self.vic_font_2.render(cst.VICTORY_2, True, cst.BL)
        self.los_font_1 = pygame.font.Font(cst.Bold_text_font, 55)
        self.los_text_1 = self.los_font_1.render(cst.GAMEOVER_1, True, cst.BL)
        self.los_font_2 = pygame.font.Font(cst.Bold_text_font, 30)
        self.los_text_2 = self.los_font_2.render(cst.GAMEOVER_2, True, cst.BL)
        # Table of the level:
        self.nb_sprite = 15
        self.sprite_size = 30
        self.font_wall = pygame.image.load(cst.WALL)
        self.font_path = pygame.image.load(cst.PATH)
        self.font_start = pygame.image.load(cst.START)
        # Characters & objects
        self.mac_gyver_img = pygame.image.load(cst.MACGYVER)
        self.mac_gyver_img.set_colorkey(cst.WHITE)
        self.font_guard = pygame.image.load(cst.GUARD)
        self.font_guard.set_colorkey(cst.WHITE)
        self.needle = pygame.image.load(cst.NEEDLE)
        self.needle.set_colorkey(cst.WHITE)
        self.tube = pygame.image.load(cst.TUBE)
        self.tube.set_colorkey(cst.WHITE)
        self.ether = pygame.image.load(cst.ETHER)
        self.ether.set_colorkey(cst.WHITE)

    def loading_page(self):
        """Method to display loading page"""
        pygame.display.set_caption(cst.WINDOW_TITLE)
        self.surface.fill(self.black)
        self.surface.blit(self.image_start,
                          [15, (int(self.window_resolution[1]) -
                                int(self.image_start.get_height())) / 2 + 10])
        self.surface.blit(self.title_menu_text, [180, 30])
        self.surface.blit(self.click_to_play, [130, 460])
        pygame.display.flip()

    def victory_page(self):
        """Method to display victory page"""
        pygame.display.set_caption(cst.WINDOW_TITLE)
        self.surface.fill(self.black)
        self.surface.blit(self.vic_text_1, [60, 150])
        self.surface.blit(self.vic_text_2, [60, 300])
        pygame.display.flip()

    def lose_page(self):
        """Method to display defeat page"""
        pygame.display.set_caption(cst.WINDOW_TITLE)
        self.surface.fill(self.black)
        self.surface.blit(self.los_text_1, [60, 150])
        self.surface.blit(self.los_text_2, [60, 300])
        pygame.display.flip()

    def game_page(self):
        """Method to display game page"""
        pygame.display.set_caption(cst.WINDOW_TITLE)
        self.surface.fill(self.black)

    def draw_path(self, x, y):
        """Method to display path in the maze"""
        self.surface.blit(self.font_path, [self.sprite_size * x,
                                           self.sprite_size * y])
        pygame.display.flip()

    def draw_wall(self, x, y):
        """Method to display wall in the maze"""
        self.surface.blit(self.font_wall, [self.sprite_size * x,
                                           self.sprite_size * y])
        pygame.display.flip()

    def draw_guard(self, x, y):
        """Method to display guard in the maze"""
        self.draw_path(x, y)
        self.surface.blit(self.font_guard, [self.sprite_size * x,
                                            self.sprite_size * y])
        pygame.display.flip()

    def draw_needle(self, x, y):
        """Method to display needle in the maze"""
        self.surface.blit(self.needle, [self.sprite_size * x,
                                        self.sprite_size * y])
        pygame.display.flip()

    def draw_tube(self, x, y):
        """Method to display tube in the maze"""
        self.surface.blit(self.tube, [self.sprite_size * x,
                                      self.sprite_size * y])
        pygame.display.flip()

    def draw_ether(self, x, y):
        """Method to display ether in the maze"""
        self.surface.blit(self.ether, [self.sprite_size * x,
                                       self.sprite_size * y])
        pygame.display.flip()

    def draw_macgyver(self, x, y):
        """Method to display Mac Gyver in the maze"""
        self.draw_path(x, y)
        self.surface.blit(self.mac_gyver_img, [self.sprite_size * x,
                                               self.sprite_size * y])
        pygame.display.flip()

    def advance_mac(self, x, y, new_pos):
        """Method to display Mac Gyver displacement"""
        self.draw_path(x, y)
        self.draw_macgyver(new_pos[0], new_pos[1])
        pygame.display.flip()
