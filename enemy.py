import random
from board import Board
from game import Game


class Enemy:
    def __init__(self, site):
        self.site = site


class EasyEnemy(Enemy):
    def __init__(self, site):
        super().__init__(site)

    def make_move(self, board: Board, game: Game):
        selected_piece = random.choice(('x', 'o'))
        selected_square = None
        while not selected_square:
            x = random.randint(0, 5)
            y = random.randint(0, 5)
            if game.game_status[x][y] == 0:
                selected_square = (x, y)
        game.game_status[x][y] = selected_piece
        board.draw_move(selected_piece, selected_square)
        game.reset()


class HardEnemy(Enemy):
    def __init__(self, site):
        super().__init__(site)

    def make_move(self, board: Board, game: Game):
        if self.site == 'chaos':
            pairs = {'00': '55', '01': '45', '02': '03', '03': '02',
                     '04': '40', '05': '50', '10': '54', '11': '13',
                     '12': '32', '13': '11', '14': '34', '15': '51',
                     '20': '30', '21': '41', '22': '24', '23': '43',
                     '24': '22', '25': '35', '30': '20', '31': '33',
                     '32': '12', '33': '31', '34': '14', '35': '25',
                     '40': '04', '41': '21', '42': '44', '43': '23',
                     '44': '42', '45': '01', '50': '05', '51': '15',
                     '52': '53', '53': '52', '54': '01', '55': '00'}
            enemy_token = game.last_move[0]
            enemy_square = game.last_move[1]
            square = (int(pairs[enemy_square][0]), int(pairs[enemy_square][1]))
            if enemy_square in ('00', '05', '50', '55'):
                token = enemy_token
            else:
                token = 'x' if enemy_token == 'o' else 'o'
            game.game_status[square[0]][square[1]] = token
            board.draw_move(token, square)
            game.reset()
        elif self.site == 'order':
            pass
