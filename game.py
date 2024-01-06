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
        self.last_move = None

    def check_endgame(self):
        gm = self.game_status

        # check if order won horizontally
        for row in gm:
            if row.count('x') == 5 and not (row[0] == row[5] == 'x'):
                self.board.endgame('order')
                return True  # order won
            if row.count('o') == 5 and not (row[0] == row[5] == 'o'):
                self.board.endgame('order')
                return True  # order won

        # check if order won vertically
        for index in range(6):
            column = [row[index] for row in gm]
            if column.count('x') == 5 and not (column[0] == column[5] == 'x'):
                self.board.endgame('order')
                return True  # order won
            if column.count('o') == 5 and not (column[0] == column[5] == 'o'):
                self.board.endgame('order')
                return True  # order won

        # check if order won diagonally
        six_in_row_00_55 = (gm[0][0] == gm[1][1] == gm[2][2] == gm[3][3] ==
                            gm[4][4] == gm[5][5] != 0)
        six_in_row_05_50 = (gm[0][5] == gm[1][4] == gm[2][3] == gm[3][2] ==
                            gm[4][1] == gm[5][0] != 0)

        diagonal_win_combinations = [['04', '13', '22', '31', '40'],
                                     ['05', '14', '23', '32', '41'],
                                     ['14', '23', '32', '41', '50'],
                                     ['15', '24', '33', '42', '51'],
                                     ['00', '11', '22', '33', '44'],
                                     ['01', '12', '23', '34', '45'],
                                     ['10', '21', '32', '43', '54'],
                                     ['11', '22', '33', '44', '55']]
        for comb in diagonal_win_combinations:
            first_square = gm[int(comb[0][0])][int(comb[0][1])]
            if all(gm[int(x[0])][int(x[1])] == first_square for x in comb):
                zero_occurences = 0
                for square in comb:
                    if gm[int(square[0])][int(square[1])] == 0:
                        zero_occurences += 1
                if not zero_occurences:
                    if not (six_in_row_00_55 or six_in_row_05_50):
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

    def move_validation(self, square):
        x = square[0]
        y = square[1]
        if not self.game_status[x][y] == 0:
            self.selected_square = None
            return False
        return True

    def reset(self):
        self.selected_piece = None
        self.selected_square = None
        self.player_turn = not self.player_turn

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
            if self.move_validation(self.selected_square):
                selected_x = self.selected_square[0]
                selected_y = self.selected_square[1]
                self.game_status[selected_x][selected_y] = self.selected_piece
                self.board.draw_move(self.selected_piece, self.selected_square)
                if not self.check_endgame():
                    x = self.selected_square[0]
                    y = self.selected_square[1]
                    square_str = str(x) + str(y)
                    self.last_move = (self.selected_piece, square_str)
                    self.reset()
