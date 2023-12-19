from menu import Menu
from board import Board
from enemy import EasyEnemy, HardEnemy
from game import Game
import pygame
pygame.init()
pygame.font.init()


def main():
    screen = pygame.display.set_mode((1200, 700))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Porządek i chaos')
    menu = Menu(screen)
    menu.draw()

    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

        if menu.starter():
            menu.before_game = False
            menu.ingame(menu.choosen_site, menu.choosen_level)
            board = Board(screen)
            board.draw_board()
            game = Game(menu.choosen_site, menu.choosen_level, board, screen)
            if game.site == 'chaos':
                enemy_site = 'order'
            elif game.site == 'order':
                enemy_site = 'chaos'
            if game.level == 'easy':
                enemy = EasyEnemy(enemy_site)
            elif game.level == 'hard':
                enemy = HardEnemy(enemy_site)

        if not menu.before_game:
            if game.player_turn:
                game.make_move()
            else:
                enemy.make_move(board, game)
    pygame.quit()


if __name__ == '__main__':
    main()
