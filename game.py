from menu import TextSurface
from board import Board
from constants import montserrat_font, colors
import pygame
import math


class Game:
    def __init__(self, site, level, board: Board):
        self.game_status = [[0 for _ in range(6)] for _ in range(6)]
        self.site = site
        if self.site == 'order':
            self.player_turn = True
        else:
            self.player_turn = False
        self.level = level
        self.selected_piece = None
        self.selected_square = None
        self.board = board

    def move_consequences(self):
        pass

    def move_validation(self, screen):
        x = self.selected_square[0]
        y = self.selected_square[1]
        if self.game_status[x][y] != 0:
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
        if self.player_turn is True:
            self.player_turn = False
        else:
            self.player_turn = True

    def make_move(self, screen):
        if self.board.x_button.isclicked():
            self.selected_piece = 'x'
        if self.board.o_button.isclicked():
            self.selected_piece = 'o'

        if self.selected_piece and pygame.mouse.get_pressed()[0] == 1:
            pos = pygame.mouse.get_pos()
            start_x = self.board.start_coords[0]
            start_y = self.board.start_coords[1]
            end_x = start_x + self.board.size[0]
            end_y = start_y + self.board.size[1]
            if pos[0] >= start_x and pos[0] <= end_x:
                if pos[1] >= start_y and pos[1] <= end_y:
                    row = math.floor((pos[0] - 50) / 100)
                    column = math.floor((pos[1] - 50) / 100)
                    self.selected_square = (row, column)

        if self.selected_piece and self.selected_square:
            if self.move_validation(screen):
                selected_x = self.selected_square[0]
                selected_y = self.selected_square[1]
                self.game_status[selected_x][selected_y] = self.selected_piece
                self.board.draw_move(self.selected_piece, self.selected_square,
                                     screen)
                self.reset()
                return True
