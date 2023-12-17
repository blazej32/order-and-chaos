from menu import Menu
from board import Board
import pygame
pygame.init()
pygame.font.init()

# constants
fonts = {80: pygame.font.Font('montserrat.ttf', 80),
         40: pygame.font.Font('montserrat.ttf', 40),
         30: pygame.font.Font('montserrat.ttf', 30),
         20: pygame.font.Font('montserrat.ttf', 20)}
colors = colors = {'white': (249, 245, 235),
                   'blue': (0, 43, 91),
                   'red': (234, 84, 85),
                   'gray': (75, 76, 77)}


# create screen
screen_size = (1200, 700)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Porządek i chaos')

# draw menu
game_menu = Menu(fonts, colors)
game_menu.draw(screen)


# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

    if game_menu.starter():
        game_board = Board(fonts, colors, game_menu.choosen_site,
                           game_menu.choosen_level)
        game_board.draw(screen)


pygame.quit()
