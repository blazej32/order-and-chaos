import pygame

colors = {'white': (249, 245, 235),
          'blue': (0, 43, 91),
          'red': (234, 84, 85),
          'gray': (75, 76, 77)}

screen_size = (1200, 700)


def montserrat_font(size):
    return pygame.font.Font('montserrat.ttf', size)
