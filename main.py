# from board import Board
import pygame
pygame.init()
pygame.font.init()

screen_size = (800, 1000)
main_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Porządek i chaos')

main_font = pygame.font.SysFont 
colors = {'white': (249, 245, 235),
          'blue': (0, 43, 91),
          'red': (234, 84, 85),
          'gray': (75, 76, 77)
          }
main_screen.fill(colors['white'])
pygame.display.flip()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
