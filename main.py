import pygame
pygame.init()
pygame.font.init()

# set up constants
ms_font = pygame.font.Font('rubik_doodle_shadow.ttf', 60)
screen_size = (800, 1000)
colors = {'white': (249, 245, 235),
          'blue': (0, 43, 91),
          'red': (234, 84, 85),
          'gray': (75, 76, 77)
          }

# create main menu screen with all surfaces
ms = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Porządek i chaos')
ms.fill(colors['white'])


class TextSurf:
    def __init__(self, msg, font, color, location, screen):
        self.msg = msg
        self.font = font
        self.color = color
        self.location = location
        self.screen = screen

    def draw(self):
        surf = self.font.render(self.msg, False, self.color)
        self.screen.blit(surf, self.location)


site_choice = TextSurf('wybierz stronę', ms_font, colors['gray'], (150, 100), ms)
site_choice.draw()

level = TextSurf('POZIOM TRUDNOŚCI', ms_font, colors['gray'], (100, 400), ms)
level.draw()

# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
