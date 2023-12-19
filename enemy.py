import random
from board import Board


class Enemy:
    def __init__(self, site):
        self.site = site


class EasyEnemy(Enemy):
    def __init__(self):
        super().__init__()

    def make_move(self, board: Board):
        selected_piece = random.choice(('x', 'o'))
        selected_square = None
        while not selected_square:
            x = random.randint(0, 5)
            y = random.randint(0, 5)
            if board.game[x][y] == 0:
                selected_square = (x, y)
        board.game[x][y] = selected_piece


class HardEnemy(Enemy):
    def __init__(self):
        super().__init__()

    def make_move(self, game):
        pass
