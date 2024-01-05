from menu import Menu
from board import Board
from enemy import Enemy, BoostedEnemy
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
            map_enemy_site = {'chaos': 'order', 'order': 'chaos'}
            if game.level == 'easy':
                enemy = Enemy(map_enemy_site[game.site], board, game)
            elif game.level == 'hard':
                enemy = BoostedEnemy(map_enemy_site[game.site], board, game)

        if not menu.before_game:
            if game.player_turn:
                game.make_move()
            else:
                pygame.time.wait(500)
                enemy.make_move()
    pygame.quit()


if __name__ == '__main__':
    main()
