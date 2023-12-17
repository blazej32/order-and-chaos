import pygame
from menu import TextSurface, Button
from constants import montserrat_font


class Board():
    def __init__(self, colors, site, level):
        self.colors = colors
        self.site = site
        self.level = level
        self.selected_piece = None
        self.game = [[0 for x in range(6)] for y in range(6)]
        self.x_button = Button((750, 475), (150, 150), self.colors['red'])
        self.o_button = Button((950, 475), (150, 150), self.colors['blue'])

    def draw(self, screen):
        white = self.colors['white']
        pygame.draw.rect(screen, white, (0, 0, 1200, 700))
        for line in range(7):
            height = line * 100 + 50
            start_coords = (50, height)
            end_coords = (650, height)
            pygame.draw.line(screen, self.colors['gray'], start_coords,
                             end_coords, 5)
            pygame.draw.line(screen, self.colors['gray'],
                             (start_coords[1], start_coords[0]),
                             (end_coords[1], end_coords[0]), 5)
        if self.site == 'order':
            site_info = TextSurface('grasz jako porządek', montserrat_font(30),
                                    (750, 50), self.colors['gray'])
            site_info.draw(screen)
        if self.site == 'chaos':
            site_info = TextSurface('grasz jako chaos', montserrat_font(30),
                                    (750, 50), self.colors['gray'])
            site_info.draw(screen)
        if self.level == 'easy':
            level_info = TextSurface('poziom: łatwy', montserrat_font(30),
                                     (750, 100), self.colors['gray'])
            level_info.draw(screen)
        if self.level == 'hard':
            level_info = TextSurface('poziom: trudny', montserrat_font(30),
                                     (750, 100), self.colors['gray'])
            level_info.draw(screen)

        self.x_button.draw(screen)
        self.o_button.draw(screen)
        x_but_msg = TextSurface('X', montserrat_font(130), (775, 472), white)
        x_but_msg.draw(screen)
        o_but_msg = TextSurface('O', montserrat_font(130), (970, 470), white)
        o_but_msg.draw(screen)
