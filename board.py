import pygame
from menu import TextSurface, Button
from constants import montserrat_font
from constants import colors


class Board():
    def __init__(self):
        pass

    def draw(self, screen):
        for line in range(7):
            height = line * 100 + 50
            start_coords = (50, height)
            end_coords = (650, height)
            pygame.draw.line(screen, colors['gray'], start_coords,
                             end_coords, 5)
            pygame.draw.line(screen, colors['gray'],
                             (start_coords[1], start_coords[0]),
                             (end_coords[1], end_coords[0]), 5)

    def move_validation(self):
        return True

    def make_move(self):
        if self.x_button.isclicked():
            self.selected_piece == 'x'
        if self.o_button.isclicked():
            self.selected_piece == 'o'

        if self.selected_piece and pygame.mouse.get_pressed()[0] == 1:
            pass
