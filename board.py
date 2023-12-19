import pygame
import math
from constants import colors, montserrat_font
from menu import TextSurface, Button


class Board():
    def __init__(self, site, level):
        self.start_coords = (50, 50)
        self.size = (600, 600)
        self.x_button = Button((750, 475), (150, 150), colors['red'])
        self.o_button = Button((950, 475), (150, 150), colors['blue'])
        self.game = [[0 for _ in range(6)] for _ in range(6)]
        self.selected_piece = None
        self.selected_square = None
        self.site = site
        if self.site == 'order':
            self.player_turn = True
        else:
            self.player_turn = False
        self.level = level

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
        self.x_button.draw(screen)
        self.o_button.draw(screen)
        x_but_msg = TextSurface('X', montserrat_font(130), (775, 472),
                                colors['white'])
        x_but_msg.draw(screen)
        o_but_msg = TextSurface('O', montserrat_font(130), (970, 470),
                                colors['white'])
        o_but_msg.draw(screen)

    def move_consequences(self):
        pass

    def move_validation(self, screen):
        if self.game[self.selected_square[0]][self.selected_square[1]] != 0:
            error_msg = TextSurface('square already taken',
                                    montserrat_font(30), (750, 150),
                                    colors['gray'])
            error_msg.draw(screen)
            self.selected_piece = None
            self.selected_square = None
            return False
        return True

    def reset(self):
        self.selected_piece = None
        self.selected_square = None
        # self.player_turn = False

    def draw_move(self, piece, square, screen):
        piece_text_x = square[0] * 100 + 67
        piece_text_y = square[1] * 100 + 31
        if piece == 'x':
            draw_piece = TextSurface('x', montserrat_font(100),
                                     (piece_text_x, piece_text_y),
                                     colors['red'])
        elif piece == 'o':
            draw_piece = TextSurface('o', montserrat_font(100),
                                     (piece_text_x, piece_text_y),
                                     colors['blue'])
        draw_piece.draw(screen)

    def make_move(self, screen):
        if self.x_button.isclicked():
            self.selected_piece = 'x'
        if self.o_button.isclicked():
            self.selected_piece = 'o'

        if self.selected_piece and pygame.mouse.get_pressed()[0] == 1:
            pos = pygame.mouse.get_pos()
            start_x = self.start_coords[0]
            start_y = self.start_coords[1]
            end_x = start_x + self.size[0]
            end_y = start_y + self.size[1]
            if pos[0] >= start_x and pos[0] <= end_x:
                if pos[1] >= start_y and pos[1] <= end_y:
                    row = math.floor((pos[0] - 50) / 100)
                    column = math.floor((pos[1] - 50) / 100)
                    self.selected_square = (row, column)

        if self.selected_piece and self.selected_square:
            if self.move_validation(screen):
                selected_x = self.selected_square[0]
                selected_y = self.selected_square[1]
                self.game[selected_x][selected_y] = self.selected_piece
                self.draw_move(self.selected_piece, (selected_x, selected_y),
                               screen)
                self.reset()
