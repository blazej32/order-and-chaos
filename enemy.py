import random
from board import Board
from game import Game


class Enemy:
    def __init__(self, site):
        self.site = site

    def move_execution(self, square, token, board: Board, game: Game):
        game.game_status[square[0]][square[1]] = token
        board.draw_move(token, square)
        game.check_endgame()
        game.reset()


class EasyEnemy(Enemy):
    def __init__(self, site):
        super().__init__(site)

    def make_move(self, board: Board, game: Game):
        token = random.choice(('x', 'o'))
        square = None
        while not square:
            x = random.randint(0, 5)
            y = random.randint(0, 5)
            if game.game_status[x][y] == 0:
                square = (x, y)
        self.move_execution(square, token, board, game)


class HardEnemy(Enemy):
    def __init__(self, site):
        super().__init__(site)

    def make_move(self, board: Board, game: Game):
        gs = game.game_status
        if self.site == 'chaos':
            enemy_square = game.last_move[1]
            enemy_token = game.last_move[0]
            # check diagonals (four cases)
            # case 1: 00-55 open 3
            if gs[0][0] == gs[5][5] == 0:
                diagonal = [gs[1][1], gs[2][2], gs[3][3], gs[4][4]]
                if diagonal.count('x') == 3 and diagonal.count(0) == 1:
                    self.move_execution((0, 0), 'o', board, game)
                if diagonal.count('o') == 3 and diagonal.count(0) == 1:
                    self.move_execution((0, 0), 'x', board, game)
            # case 2: 05-50 open 3
            if gs[0][5] == gs[5][0] == 0:
                diagonal = [gs[1][4], gs[2][3], gs[3][2], gs[4][1]]
                if diagonal.count('x') == 3 and diagonal.count(0) == 1:
                    self.move_execution((0, 5), 'o', board, game)
                if diagonal.count('o') == 3 and diagonal.count(0) == 1:
                    self.move_execution((0, 5), 'x', board, game)
            # case 3: 00-55 open 4
            if gs[1][1] == gs[2][2] == gs[3][3] == gs[4][4]:
                if gs[1][1] == 'x':
                    if gs[0][0] == 0:
                        self.move_execution((0, 0), 'o', board, game)
                    else:
                        self.move_execution((5, 5), 'o', board, game)
                elif gs[1][1] == 'o':
                    if gs[0][0] == 0:
                        self.move_execution((0, 0), 'x', board, game)
                    else:
                        self.move_execution((5, 5), 'o', board, game)
            # case 4: 05-50 open 4
            if gs[1][4] == gs[2][3] == gs[3][2] == gs[4][1]:
                if gs[1][4] == 'x':
                    if gs[0][5] == 0:
                        self.move_execution((0, 5), 'o', board, game)
                    else:
                        self.move_execution((5, 0), 'o', board, game)
                elif gs[1][4] == 'o':
                    if gs[0][5] == 0:
                        self.move_execution((0, 5), 'x', board, game)
                    else:
                        self.move_execution((5, 0), 'x', board, game)

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
            self.move_execution((column, row), token, board, game)
        elif self.site == 'order':
            if all(row.count(0) == 6 for row in gs):
                token = random.choice(('x', 'o'))
                row = random.randint(2, 3)
                column = random.randint(2, 3)
                square = (column, row)
                self.move_execution(square, token, board, game)
                return True

            enemy_token = game.last_move[0]
            enemy_square = game.last_move[1]

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
                self.move_execution((column, row), token, board, game)
