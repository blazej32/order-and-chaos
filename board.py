import pygame
from constants import WHITE, BLUE, RED, GRAY
from menu import TextSurface, Button


class Board():
    def __init__(self):
        self.start_coords = (50, 50)
        self.size = (600, 600)
        self.x_button = Button((750, 475), (150, 150), RED)
        self.o_button = Button((950, 475), (150, 150), BLUE)

    def draw_board(self, screen):
        for line in range(7):
            height = line * 100 + 50
            start_coords = (50, height)
            end_coords = (650, height)
            pygame.draw.line(screen, GRAY, start_coords, end_coords, 5)
            pygame.draw.line(screen, GRAY, (start_coords[1], start_coords[0]),
                             (end_coords[1], end_coords[0]), 5)
        self.x_button.draw(screen)
        self.o_button.draw(screen)
        x_but_msg = TextSurface('X', 130, (775, 472), WHITE)
        x_but_msg.draw(screen)
        o_but_msg = TextSurface('O', 130, (970, 470), WHITE)
        o_but_msg.draw(screen)

    def draw_move(self, piece, square, screen):
        piece_text_x = square[0] * 100 + 67
        piece_text_y = square[1] * 100 + 31
        if piece == 'x':
            draw_pc = TextSurface('x', 100, (piece_text_x, piece_text_y), RED)
        elif piece == 'o':
            draw_pc = TextSurface('o', 100, (piece_text_x, piece_text_y), BLUE)
        draw_pc.draw(screen)
