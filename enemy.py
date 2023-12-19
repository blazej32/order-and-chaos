import random
import pygame
from board import Board
from game import Game


class Enemy:
    def __init__(self, site):
        self.site = site


class EasyEnemy(Enemy):
    def __init__(self, site):
        super().__init__(site)

    def make_move(self, board: Board, game: Game, screen):
        pygame.time.wait(1000)
        selected_piece = random.choice(('x', 'o'))
        selected_square = None
        while not selected_square:
            x = random.randint(0, 5)
            y = random.randint(0, 5)
            if game.game_status[x][y] == 0:
                selected_square = (x, y)
        game.game_status[x][y] = selected_piece
        board.draw_move(selected_piece, selected_square, screen)
        game.reset()


class HardEnemy(Enemy):
    def __init__(self, site):
        super().__init__(site)

    def make_move(self, board: Board, game):
        pass
