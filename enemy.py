import random
from board import Board
from game import Game


class Enemy:
    def __init__(self, site, board: Board, game: Game):
        self.site = site
        self.board = board
        self.game = game

    def move_execution(self, square, token):
        self.game.game_status[square[0]][square[1]] = token
        self.board.draw_move(token, square)
        self.game.check_endgame()
        self.game.reset()

    def make_move(self):
        token = random.choice(('x', 'o'))
        square = None
        while not square:
            x = random.randint(0, 5)
            y = random.randint(0, 5)
            if self.game.game_status[x][y] == 0:
                square = (x, y)
        self.move_execution(square, token)


class BoostedEnemy(Enemy):
    def __init__(self, site, board, game):
        super().__init__(site, board, game)

    def make_move(self):
        first_try = self.find_move()
        if self.game.move_validation(first_try[0]):
            self.move_execution(first_try[0], first_try[1])
        else:
            super().make_move()

    def check_open_four(self, lst):
        if lst[0] == lst[5]:
            return False
        # check for x
        if lst.count('x') == 4 and lst.count(0) >= 1:
            if lst[0] == 'x':
                if lst[5] == 0:
                    return (5, 'x')
                elif lst[5] == 'o':
                    return (lst.index(0), 'o')
            elif lst[5] == 'x':
                if lst[0] == 0:
                    return (0, 'x')
                elif lst[0] == 'o':
                    return (lst.index(0), 'o')

        # check for o
        if lst.count('o') == 4 and lst.count(0) >= 1:
            if lst[0] == 'o':
                if lst[5] == 0:
                    return (5, 'o')
                elif lst[5] == 'x':
                    return (lst.index(0), 'x')
            elif lst[5] == 'o':
                if lst[0] == 0:
                    return (0, 'o')
                elif lst[0] == 'x':
                    return (lst.index(0), 'x')
        return False

    def check_open_three(self, list):
        if list[0] == list[5] == 0:
            centre = list[1:5]
            # check for x
            if centre.count('x') == 3 and centre.count(0) == 1:
                return (centre.index(0) + 1, 'x')
            # check for o
            if centre.count('o') == 3 and centre.count(0) == 1:
                return (centre.index(0) + 1, 'o')
        return False

    def check_forced_win(self, lst):
        centre = lst[1:5]
        if lst.count('x') == 4 and 'o' not in centre:
            if lst[0] == lst[5] == 0 or lst[0] != lst[5]:
                return (lst.index(0), 'x')
        if lst.count('o') == 4 and 'x' not in centre:
            if lst[0] == lst[5] == 0 or lst[0] != lst[5]:
                return (lst.index(0), 'o')
        return False

    def inner_square_evaluation(self, square):
        gs = self.game.game_status
        o_points = 0
        x_points = 0
        rng_15 = range(1, 5)
        rows = [[str(x) + str(y) for x in rng_15] for y in rng_15]
        columns = [[str(y) + str(x) for x in rng_15] for y in rng_15]
        diagonals = [['11', '22', '33', '44'],
                     ['14', '23', '32', '41']]
        zeros_to_points = {4: 3, 3: 4, 2: 5, 1: 1000}

        # 1. check row, column, diagonal for o
        for row in rows:
            if square in row:
                row_values = [gs[int(x[0])][int(x[1])] for x in row]
                if 'x' in row_values and 'o' in row_values:
                    break
                if 'x' in row_values:
                    x_points += zeros_to_points[row_values.count(0)]
                else:
                    o_points += zeros_to_points[row_values.count(0)]

        for column in columns:
            if square in column:
                column_values = [gs[int(x[0])][int(x[1])] for x in column]
                if 'x' in column_values and 'o' in column_values:
                    break
                if 'x' in column_values:
                    x_points += zeros_to_points[column_values.count(0)]
                else:
                    o_points += zeros_to_points[column_values.count(0)]

        for diagonal in diagonals:
            if square in diagonal:
                diagonal_values = [gs[int(x[0])][int(x[1])] for x in diagonal]
                if 'x' in diagonal_values and 'o' in diagonal_values:
                    break
                if 'x' in diagonal_values:
                    x_points += zeros_to_points[diagonal_values.count(0)]
                else:
                    o_points += zeros_to_points[diagonal_values.count(0)]

        # 3. return the one with more points
        points = o_points if o_points >= x_points else x_points
        token = 'o' if o_points >= x_points else 'x'
        return (points, square, token)

    def inner_sqares_left(self):
        gs = self.game.game_status
        inner = [[gs[x][y] for x in range(1, 5)] for y in range(1, 5)]
        for row in inner:
            if 0 in row:
                return True
        return False

    def find_move(self):
        gs = self.game.game_status
        diagonal_00_55 = [gs[0][0], gs[1][1], gs[2][2], gs[3][3], gs[4][4],
                          gs[5][5]]
        diagonal_05_50 = [gs[0][5], gs[1][4], gs[2][3], gs[3][2], gs[4][1],
                          gs[5][0]]
        diagonal_10_54 = {'10': gs[1][0], '21': gs[2][1], '32': gs[3][2],
                          '43': gs[4][3], '54': gs[5][4]}
        diagonal_01_45 = {'01': gs[0][1], '12': gs[1][2], '23': gs[2][3],
                          '34': gs[3][4], '45': gs[4][5]}
        diagonal_04_40 = {'04': gs[0][4], '13': gs[1][3], '22': gs[2][2],
                          '31': gs[3][1], '40': gs[4][0]}
        diagonal_15_51 = {'15': gs[1][5], '24': gs[2][4], '33': gs[3][3],
                          '42': gs[4][2], '51': gs[5][1]}

        if self.site == 'chaos':
            enemy_square = self.game.last_move[1]
            enemy_token = self.game.last_move[0]

            # check main diagonals open fours
            if diagonal_00_55.count('x') == 4 and diagonal_00_55.count(0) == 1:
                square = (diagonal_00_55.index(0), diagonal_00_55.index(0))
                return (square, 'o')
            if diagonal_00_55.count('o') == 4 and diagonal_00_55.count(0) == 1:
                square = (diagonal_00_55.index(0), diagonal_00_55.index(0))
                return (square, 'x')
            if diagonal_05_50.count('x') == 4 and diagonal_05_50.count(0) == 1:
                square = (diagonal_05_50.index(0), 5 - diagonal_05_50.index(0))
                return (square, 'o')
            if diagonal_05_50.count('o') == 4 and diagonal_05_50.count(0) == 1:
                square = (diagonal_05_50.index(0), 5 - diagonal_05_50.index(0))
                return (square, 'x')

            # check small diagonals open fours
            dg = diagonal_10_54
            dg_values = list(dg.values())
            dg_keys = list(dg.keys())
            if dg_values.count('x') == 4 and dg_values.count(0) == 1:
                str_square = dg_keys[dg_values.index(0)]
                square = (int(str_square[0]), int(str_square[1]))
                return (square, 'o')
            if dg_values.count('o') == 4 and dg_values.count(0) == 1:
                str_square = dg_keys[dg_values.index(0)]
                square = (int(str_square[0]), int(str_square[1]))
                return (square, 'x')

            dg = diagonal_01_45
            dg_values = list(dg.values())
            dg_keys = list(dg.keys())
            if dg_values.count('x') == 4 and dg_values.count(0) == 1:
                str_square = dg_keys[dg_values.index(0)]
                square = (int(str_square[0]), int(str_square[1]))
                return (square, 'o')
            if dg_values.count('o') == 4 and dg_values.count(0) == 1:
                str_square = dg_keys[dg_values().index(0)]
                square = (int(str_square[0]), int(str_square[1]))
                return (square, 'x')

            dg = diagonal_04_40
            dg_values = list(dg.values())
            dg_keys = list(dg.keys())
            if dg_values.count('x') == 4 and dg_values.count(0) == 1:
                str_square = dg_keys[dg_values().index(0)]
                square = (int(str_square[0]), int(str_square[1]))
                return (square, 'o')
            if dg_values.count('o') == 4 and dg_values.count(0) == 1:
                str_square = dg_keys[dg_values().index(0)]
                square = (int(str_square[0]), int(str_square[1]))
                return (square, 'x')

            dg = diagonal_15_51
            dg_values = list(dg.values())
            dg_keys = list(dg.keys())
            if dg_values.count('x') == 4 and dg_values.count(0) == 1:
                str_square = dg_keys[dg_values.index(0)]
                square = (int(str_square[0]), int(str_square[1]))
                return (square, 'o')
            if dg_values.count('o') == 4 and dg_values.count(0) == 1:
                str_square = dg_keys[dg_values.index(0)]
                square = (int(str_square[0]), int(str_square[1]))
                return (square, 'x')

            # check row and columns open fours
            for col_index in range(6):
                column = [row[col_index] for row in gs]
                check_fours = self.check_open_four(column)
                if isinstance(check_fours, tuple):
                    square = (check_fours[0], col_index)
                    token = check_fours[1]
                    return (square, token)

            for row_index in range(6):
                check_fours = self.check_open_four(gs[row_index])
                if isinstance(check_fours, tuple):
                    square = (row_index, check_fours[0])
                    token = check_fours[1]
                    return (square, token)

            # check row and column open threes
            for col_index in range(6):
                column = [row[col_index] for row in gs]
                check_threes = self.check_open_three(column)
                if isinstance(check_threes, tuple):
                    square = (check_threes[0], col_index)
                    token = check_threes[1]
                    return (square, token)

            for row_index in range(6):
                check_threes = self.check_open_three(gs[row_index])
                if isinstance(check_threes, tuple):
                    square = (row_index, check_threes[0])
                    token = check_threes[1]
                    return (square, token)

            # 00-55 open 3
            if gs[0][0] == gs[5][5] == 0:
                diagonal = diagonal_00_55[1:5]
                if diagonal.count('x') == 3 and diagonal.count(0) == 1:
                    return ((0, 0), 'o')
                if diagonal.count('o') == 3 and diagonal.count(0) == 1:
                    return ((0, 0), 'x')
            # 05-50 open 3
            if gs[0][5] == gs[5][0] == 0:
                diagonal = diagonal_05_50[1:5]
                if diagonal.count('x') == 3 and diagonal.count(0) == 1:
                    return ((0, 5), 'o')
                if diagonal.count('o') == 3 and diagonal.count(0) == 1:
                    return ((0, 5), 'x')

            # classic pairs
            pairs = {'00': '55', '01': '45', '02': '03', '03': '02',
                     '04': '40', '05': '50', '10': '54', '11': '13',
                     '12': '32', '13': '11', '14': '34', '15': '51',
                     '20': '30', '21': '41', '22': '24', '23': '43',
                     '24': '22', '25': '35', '30': '20', '31': '33',
                     '32': '12', '33': '31', '34': '14', '35': '25',
                     '40': '04', '41': '21', '42': '44', '43': '23',
                     '44': '42', '45': '01', '50': '05', '51': '15',
                     '52': '53', '53': '52', '54': '01', '55': '00'}
            column = int(pairs[enemy_square][0])
            row = int(pairs[enemy_square][1])
            if enemy_square in ('00', '05', '50', '55'):
                token = enemy_token
            else:
                token = 'x' if enemy_token == 'o' else 'o'
            return ((column, row), token)

        elif self.site == 'order':

            # first move
            if all(row.count(0) == 6 for row in gs):
                token = random.choice(('x', 'o'))
                row = random.randint(2, 3)
                column = random.randint(2, 3)
                square = (column, row)
                return (square, token)

            enemy_token = self.game.last_move[0]
            enemy_square = self.game.last_move[1]

            # check for forced win for rows
            for row_index in range(6):
                win_check = self.check_forced_win(gs[row_index])
                if isinstance(win_check, tuple):
                    square = (row_index, win_check[0])
                    token = win_check[1]
                    return (square, token)

            # check for forced win for columns
            for col_index in range(6):
                column = [row[col_index] for row in gs]
                win_check = self.check_forced_win(column)
                if isinstance(win_check, tuple):
                    square = (win_check[0], col_index)
                    token = win_check[1]
                    return (square, token)

            # check for forced win for diagonal 00_55
            dg_00_55_win_check = self.check_forced_win(diagonal_00_55)
            if isinstance(dg_00_55_win_check, tuple):
                square = (dg_00_55_win_check[0], dg_00_55_win_check[0])
                token = dg_00_55_win_check[1]
                return (square, token)

            # check for forced win for diagonal 05_50
            dg_05_50_win_check = self.check_forced_win(diagonal_05_50)
            if isinstance(dg_05_50_win_check, tuple):
                square = (dg_05_50_win_check[0], 5 - dg_05_50_win_check[0])
                token = dg_05_50_win_check[1]
                return (square, token)

            # check for forced win for small diagonals
            dg = list(diagonal_10_54.values())
            if dg.count('x') == 4 and dg.count(0) == 1:
                str_square = list(diagonal_10_54.keys())[dg.index(0)]
                square = (int(str_square[0]), int(str_square[1]))
                token = 'x'
                return (square, token)
            if dg.count('o') == 4 and dg.count(0) == 1:
                str_square = list(diagonal_10_54.keys())[dg.index(0)]
                square = (int(str_square[0]), int(str_square[1]))
                token = 'o'
                return (square, token)

            dg = list(diagonal_01_45.values())
            if dg.count('x') == 4 and dg.count(0) == 1:
                str_square = list(diagonal_01_45.keys())[dg.index(0)]
                square = (int(str_square[0]), int(str_square[1]))
                token = 'x'
                return (square, token)
            if dg.count('o') == 4 and dg.count(0) == 1:
                str_square = list(diagonal_01_45.keys())[dg.index(0)]
                square = (int(str_square[0]), int(str_square[1]))
                token = 'o'
                return (square, token)

            dg = list(diagonal_04_40.values())
            if dg.count('x') == 4 and dg.count(0) == 1:
                str_square = list(diagonal_04_40.keys())[dg.index(0)]
                square = (int(str_square[0]), int(str_square[1]))
                token = 'x'
                return (square, token)
            if dg.count('o') == 4 and dg.count(0) == 1:
                str_square = list(diagonal_04_40.keys())[dg.index(0)]
                square = (int(str_square[0]), int(str_square[1]))
                token = 'o'
                return (square, token)

            dg = list(diagonal_15_51.values())
            if dg.count('x') == 4 and dg.count(0) == 1:
                str_square = list(diagonal_15_51.keys())[dg.index(0)]
                square = (int(str_square[0]), int(str_square[1]))
                token = 'x'
                return (square, token)
            if dg.count('o') == 4 and dg.count(0) == 1:
                str_square = list(diagonal_15_51.keys())[dg.index(0)]
                square = (int(str_square[0]), int(str_square[1]))
                token = 'o'
                return (square, token)

            # check if enemy played edge/corner
            corner_edge_pairs = {'00': '55', '01': '51', '02': '52',
                                 '03': '53', '04': '54', '05': '50',
                                 '10': '15', '20': '25', '30': '35',
                                 '40': '45', '50': '05', '51': '01',
                                 '52': '02', '53': '03', '54': '04',
                                 '55': '00', '15': '10', '25': '20',
                                 '35': '30', '45': '40'}
            if enemy_square in corner_edge_pairs.keys():
                token = 'x' if enemy_token == 'o' else 'o'
                column = int(corner_edge_pairs[enemy_square][0])
                row = int(corner_edge_pairs[enemy_square][1])
                return ((column, row), token)

            # try to do 4 in a row in central 4x4
            # evaluate center squares in order to find the best one
            # best_move and inner_square_evaluation - (points, square, token)
            # if points are equal, choose square closer to the center

            if self.inner_sqares_left():
                best_move = (0, '00', 0)

                for row_index in range(1, 5):
                    for col_index in range(1, 5):
                        if gs[row_index][col_index] == 0:
                            square = str(row_index) + str(col_index)
                            evaluation = self.inner_square_evaluation(square)
                            if evaluation[0] > best_move[0]:
                                best_move = evaluation
                            elif evaluation[0] == best_move[0]:
                                ev_x_dist = abs(float(evaluation[1][0]) - 2.5)
                                ev_y_dist = abs(float(evaluation[1][1]) - 2.5)
                                evaluation_center_dist = ev_x_dist + ev_y_dist
                                bm_x_dist = abs(float(best_move[1][0]) - 2.5)
                                bm_y_dist = abs(float(best_move[1][1]) - 2.5)
                                bm_center_dist = bm_x_dist + bm_y_dist
                                if evaluation_center_dist < bm_center_dist:
                                    best_move = evaluation

                square = (int(best_move[1][0]), int(best_move[1][1]))
                token = best_move[2]
                return (square, token)

        # if all center squares are full, make random move
        return ((3, 3), 'o')
