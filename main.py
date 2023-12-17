from menu import Menu
from constants import colors, screen_size
from board import Board
import pygame
pygame.init()
pygame.font.init()

# create screen
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Porządek i chaos')

# draw menu
game_menu = Menu(colors)
game_menu.draw(screen)


# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

    if game_menu.starter():
        game_board = Board(colors, game_menu.choosen_site,
                           game_menu.choosen_level)
        game_board.draw(screen)


pygame.quit()
