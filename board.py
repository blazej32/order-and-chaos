import pygame


class Board():
    def __init__(self, fonts, colors, site, level):
        self.fonts = fonts
        self.colors = colors

    def draw(self, screen):
        for line in range(7):
            height = line * 100 + 50
            start_coords = (50, height)
            end_coords = (650, height)
            pygame.draw.line(screen, self.colors['gray'], start_coords,
                             end_coords, 5)
            pygame.draw.line(screen, self.colors['gray'],
                             (start_coords[1], start_coords[0]),
                             (end_coords[1], end_coords[0]), 5)
