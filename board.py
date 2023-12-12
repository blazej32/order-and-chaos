import pygame


class Board():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Order and chaos')
        self.surface = pygame.display.set_mode((600, 800))


board = Board()
