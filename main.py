from constants import screen_size
from menu import Menu
from board import Board
import pygame
pygame.init()
pygame.font.init()


def main():
    # create screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Porządek i chaos')

    # draw menu
    menu = Menu()
    menu.draw(screen)

    # game loop
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

        if menu.starter(screen):
            menu.before_game = False
            menu.ingame(screen, menu.choosen_site, menu.choosen_level)
            board = Board(menu.choosen_site, menu.choosen_level)
            board.draw(screen)

        if not menu.before_game:
            if board.player_turn:
                board.make_move(screen)
            else:
                pass
                # enemy makes move

    pygame.quit()


if __name__ == '__main__':
    main()
