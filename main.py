from menu import Menu
from board import Board
import pygame
pygame.init()
pygame.font.init()

# create screen
screen_size = (1200, 700)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Porządek i chaos')

# draw board
menu = Menu()
menu.draw(screen)

# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
