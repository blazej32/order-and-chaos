from constants import WHITE, BLUE, RED, GRAY
from menu import Button, TextSurface
import pygame


class Board():
    def __init__(self, screen):
        self.start_coords = (50, 50)
        self.size = (600, 600)
        self.x_button = Button((750, 475), (150, 150), RED)
        self.o_button = Button((950, 475), (150, 150), BLUE)
        self.screen = screen

    def draw_board(self):
        for line in range(7):
            height = line * 100 + 50
            start_crds = (50, height)
            end_crds = (650, height)
            pygame.draw.line(self.screen, GRAY, start_crds, end_crds, 5)
            pygame.draw.line(self.screen, GRAY, (start_crds[1], start_crds[0]),
                             (end_crds[1], end_crds[0]), 5)
        self.x_button.draw(self.screen)
        self.o_button.draw(self.screen)
        x_but_msg = TextSurface('X', 130, (775, 472), WHITE)
        x_but_msg.draw(self.screen)
        o_but_msg = TextSurface('O', 130, (970, 470), WHITE)
        o_but_msg.draw(self.screen)

    def draw_move(self, piece, square):
        piece_text_x = square[0] * 100 + 67
        piece_text_y = square[1] * 100 + 31
        if piece == 'x':
            tx = TextSurface('x', 100, (piece_text_x, piece_text_y), RED)
        elif piece == 'o':
            tx = TextSurface('o', 100, (piece_text_x, piece_text_y), BLUE)
        tx.draw(self.screen)
