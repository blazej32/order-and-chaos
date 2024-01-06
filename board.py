from colors import white, blue, gray, red
from menu import Button, write_text
import pygame


class Board():
    def __init__(self, screen, site, level):
        self.start_coords = (50, 50)
        self.size = (600, 600)
        self.x_button = Button((750, 475), (150, 150), red)
        self.o_button = Button((950, 475), (150, 150), blue)
        self.screen = screen
        self.site = site
        self.level = level

    def draw(self):
        pygame.draw.rect(self.screen, white, (0, 0, 1200, 700))
        for line in range(7):
            height = line * 100 + 50
            start_crds = (50, height)
            end_crds = (650, height)
            pygame.draw.line(self.screen, gray, start_crds, end_crds, 5)
            pygame.draw.line(self.screen, gray, (start_crds[1], start_crds[0]),
                             (end_crds[1], end_crds[0]), 5)
        self.x_button.draw(self.screen)
        self.o_button.draw(self.screen)
        write_text('X', 130, (775, 472), white, self.screen)
        write_text('O', 130, (970, 470), white, self.screen)

        map_site = {'order': 'porządek', 'chaos': 'chaos'}
        map_level = {'easy': 'łatwy', 'hard': 'trudny'}
        scr = self.screen
        write_text(f'grasz jako {map_site[self.site]}', 30, (750, 50), gray,
                   scr)
        write_text(f'poziom: {map_level[self.level]}', 30, (750, 100), gray,
                   scr)

    def draw_move(self, piece, square):
        x = square[0] * 100 + 67
        y = square[1] * 100 + 31
        color = red if piece == 'x' else blue
        write_text(piece, 100, (x, y), color, self.screen)

    def endgame(self, winner):
        pygame.draw.rect(self.screen, white, (700, 0, 1200, 700))
        if self.site == winner:
            winning_msg = 'Zwycięstwo! :D'
            write_text(winning_msg, 40, (750, 300), gray, self.screen)
        else:
            losing_msg = 'Porażka :('
            write_text(losing_msg, 40, (750, 300), gray, self.screen)
