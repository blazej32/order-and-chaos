''''
import pygame


class Board():
    def __init__(self, size=(600, 800)):
        self._size = size
        pygame.init()
        self._screen = pygame.display.set_mode(self._size)
        pygame.display.set_caption('Order and chaos')
        self._game = [[0 for x in range(6)] for y in range(6)]

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        self._size = new_size

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, new_game):
        self._game = new_game


board = Board()

if int(input()) == 0:
    pygame.quit()
'''
