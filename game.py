from colors import white, gray
from menu import write_text
from board import Board
import pygame
import math


class Game:
    def __init__(self, site, level, board: Board, screen):
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
        self.screen = screen

    def endgame(self, winner):
        pygame.draw.rect(self.screen, white, (700, 0, 1200, 700))
        if self.site == winner:
            write_text('you won! :D', 100, (700, 100), gray, self.screen)
        else:
            write_text('you lost! :(', 100, (700, 100), gray, self.screen)

    def check_endgame(self):
        gm = self.game_status

        # check if order won horizontally
        for row in gm:
            if row.count('x') == 5 and not (row[0] == row[5] == 'x'):
                self.endgame('order')
                return True  # order won
            if row.count('o') == 5 and not (row[0] == row[5] == 'o'):
                self.endgame('order')
                return True  # order won

        # check if order won vertically
        for index in range(6):
            column = [row[index] for row in gm]
            if column.count('x') == 5 and not (column[0] == column[5] == 'x'):
                self.endgame('order')
                write_text('vertically, x', 100, (700, 250), gray, self.screen)
                return True  # order won
            if column.count('o') == 5 and not (column[0] == column[5] == 'o'):
                self.endgame('order')
                write_text('vertically, o', 100, (700, 250), gray, self.screen)
                return True  # order won

        # check if order won diagonally
        diagonal_win_combinations = [[[0, 4], [1, 3], [2, 2], [3, 1], [4, 0]],
                                     [[0, 5], [1, 4], [2, 3], [3, 2], [4, 1]],
                                     [[1, 4], [2, 3], [3, 2], [4, 1], [5, 0]],
                                     [[1, 5], [2, 4], [3, 3], [4, 3], [5, 1]],
                                     [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],
                                     [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],
                                     [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]],
                                     [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]]
        for comb in diagonal_win_combinations:
            if all(gm[x[0]][x[1]] == gm[comb[0][0]][comb[0][1]] for x in comb):
                zero_occurences = 0
                for square in comb:
                    if gm[square[0]][square[1]] == 0:
                        zero_occurences += 1
                if not zero_occurences:
                    self.endgame('order')
                    return True  # order won

        # check if chaos won
        zero_occurences = 0
        for row in gm:
            zero_occurences += row.count(0)

        if not zero_occurences:
            self.endgame('chaos')
            return True  # chaos won

        return False

    def move_validation(self):
        x = self.selected_square[0]
        y = self.selected_square[1]
        if not self.game_status[x][y] == 0:
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

    def make_move(self):
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
            if self.move_validation():
                selected_x = self.selected_square[0]
                selected_y = self.selected_square[1]
                self.game_status[selected_x][selected_y] = self.selected_piece
                self.board.draw_move(self.selected_piece, self.selected_square)
                if not self.check_endgame():
                    self.reset()
