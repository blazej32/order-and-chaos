import pygame
pygame.init()
pygame.font.init()


class TextSurface:
    def __init__(self, msg, font, location, color):
        self.msg = msg
        self.font = font
        self.color = color
        self.location = location

    def draw(self, screen):
        surf = self.font.render(self.msg, False, self.color)
        screen.blit(surf, self.location)


class Menu():
    def __init__(self):
        self.fonts = {40: pygame.font.Font('montserrat.ttf', 40),
                      30: pygame.font.Font('montserrat.ttf', 30),
                      20: pygame.font.Font('montserrat.ttf', 20)}
        self.colors = {'white': (249, 245, 235),
                       'blue': (0, 43, 91),
                       'red': (234, 84, 85),
                       'gray': (75, 76, 77)}

    def draw(self, screen):
        screen.fill(self.colors['white'])
        for line in range(7):
            height = line * 100 + 50
            start_coords = (50, height)
            end_coords = (650, height)
            pygame.draw.line(screen, self.colors['gray'], start_coords,
                             end_coords, 5)
            pygame.draw.line(screen, self.colors['gray'],
                             (start_coords[1], start_coords[0]),
                             (end_coords[1], end_coords[0]), 5)

        site_choice = TextSurface('WYBIERZ STRONĘ', self.fonts[40], (730, 50),
                                  self.colors['gray'])
        site_choice.draw(screen)

        stch_com = TextSurface('(porządek rozpoczyna grę)', self.fonts[30],
                               (715, 90), self.colors['gray'])
        stch_com.draw(screen)

        pygame.draw.rect(screen, self.colors['blue'], (715, 150, 200, 100))
        pygame.draw.rect(screen, self.colors['blue'], (935, 150, 200, 100))

        order_button = TextSurface('PORZĄDEK', self.fonts[20], (753, 185),
                                   self.colors['white'])
        order_button.draw(screen)

        chaos_button = TextSurface('CHAOS', self.fonts[20], (995, 185),
                                   self.colors['white'])
        chaos_button.draw(screen)

        level_choice = TextSurface('POZIOM TRUDNOŚCI', self.fonts[40],
                                   (710, 285), self.colors['gray'])
        level_choice.draw(screen)

        pygame.draw.rect(screen, self.colors['red'], (715, 350, 200, 100))
        pygame.draw.rect(screen, self.colors['red'], (935, 350, 200, 100))

        easy_but = TextSurface('ŁATWY', self.fonts[20], (775, 385),
                               self.colors['white'])
        easy_but.draw(screen)

        hard_but = TextSurface('TRUDNY', self.fonts[20], (990, 385),
                               self.colors['white'])
        hard_but.draw(screen)

        pygame.draw.rect(screen, self.colors['gray'], (715, 550, 420, 100))
        hard_but = TextSurface('GRAJ', self.fonts[30], (880, 580),
                               self.colors['white'])
        hard_but.draw(screen)
