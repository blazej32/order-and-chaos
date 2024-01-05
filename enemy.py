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
                return (centre.index(0) + 1, 'o')
            # check for o
            if centre.count('o') == 3 and centre.count(0) == 1:
                return (centre.index(0) + 1, 'x')
        return False

    def find_move(self):
        gs = self.game.game_status
        if self.site == 'chaos':
            enemy_square = self.game.last_move[1]
            enemy_token = self.game.last_move[0]
            # check main diagonals (3 cases)
            diagonal_00_55 = [gs[0][0], gs[1][1], gs[2][2], gs[3][3], gs[4][4],
                              gs[5][5]]
            diagonal_05_50 = [gs[0][5], gs[1][4], gs[2][3], gs[3][2], gs[4][1],
                              gs[5][0]]

            # case 1: 00-55 open 3
            if gs[0][0] == gs[5][5] == 0:
                diagonal = diagonal_00_55[1:5]
                if diagonal.count('x') == 3 and diagonal.count(0) == 1:
                    return ((0, 0), 'o')
                if diagonal.count('o') == 3 and diagonal.count(0) == 1:
                    return ((0, 0), 'x')
            # case 2: 05-50 open 3
            if gs[0][5] == gs[5][0] == 0:
                diagonal = diagonal_05_50[1:5]
                if diagonal.count('x') == 3 and diagonal.count(0) == 1:
                    return ((0, 5), 'o')
                if diagonal.count('o') == 3 and diagonal.count(0) == 1:
                    return ((0, 5), 'x')
            # case 3: 00-55 or 05-50 open 4
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

            # check smaller diagonals
            diagonal_10_54 = {'10': gs[1][0], '21': gs[2][1], '32': gs[3][2],
                              '43': gs[4][3], '54': gs[5][4]}
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

            diagonal_01_45 = {'01': gs[0][1], '12': gs[1][2], '23': gs[2][3],
                              '34': gs[3][4], '45': gs[4][5]}
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

            diagonal_04_40 = {'04': gs[0][4], '13': gs[1][3], '22': gs[2][2],
                              '31': gs[3][1], '40': gs[4][0]}
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

            diagonal_15_51 = {'15': gs[1][5], '24': gs[2][4], '33': gs[3][3],
                              '42': gs[4][2], '51': gs[5][1]}
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

            # check open fours and threes
            for col_index in range(6):
                column = [row[col_index] for row in gs]
                check_fours = self.check_open_four(column)
                if isinstance(check_fours, tuple):
                    square = (check_fours[0], col_index)
                    token = check_fours[1]
                    return (square, token)
                check_threes = self.check_open_three(column)
                if isinstance(check_threes, tuple):
                    square = (check_threes[0], col_index)
                    token = check_threes[1]
                    return (square, token)

            for row_index in range(6):
                check_fours = self.check_open_four(gs[row_index])
                if isinstance(check_fours, tuple):
                    square = (row_index, check_fours[0])
                    token = check_fours[1]
                    return (square, token)
                check_threes = self.check_open_three(gs[row_index])
                if isinstance(check_threes, tuple):
                    square = (row_index, check_threes[0])
                    token = check_threes[1]
                    return (square, token)

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
            if all(row.count(0) == 6 for row in gs):
                token = random.choice(('x', 'o'))
                row = random.randint(2, 3)
                column = random.randint(2, 3)
                square = (column, row)
                return (square, token)

            enemy_token = self.game.last_move[0]
            enemy_square = self.game.last_move[1]

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
