from constants import screen_size
from menu import Menu
from board import Board
import pygame
pygame.init()
pygame.font.init()

# create screen
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Porządek i chaos')

# draw menu
menu = Menu()
menu.draw(screen)


# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

    if menu.starter(screen):
        menu.before_game = False
        menu.ingame(screen, menu.choosen_site, menu.choosen_level)
        board = Board()
        board.draw(screen)

pygame.quit()
