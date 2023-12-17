from constants import montserrat_font
import pygame
pygame.init()
pygame.font.init()


class TextSurface:
    def __init__(self, msg, font, location, color):
        self.msg = msg
        self.color = color
        self.font = font
        self.location = location

    def draw(self, screen):
        surf = self.font.render(self.msg, False, self.color)
        screen.blit(surf, self.location)


class Button():
    def __init__(self, coords, size, color):
        self.coordinates = coords
        self.size = size
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.coordinates[0],
                         self.coordinates[1], self.size[0], self.size[1]))

    def isclicked(self):
        if pygame.mouse.get_pressed()[0] == 1:
            pos = pygame.mouse.get_pos()
            start_x = self.coordinates[0]
            end_x = self.coordinates[0] + self.size[0]
            start_y = self.coordinates[1]
            end_y = self.coordinates[1] + self.size[1]
            if pos[0] >= start_x and pos[0] <= end_x:
                if pos[1] >= start_y and pos[1] < end_y:
                    return True
        return False


class Menu():
    def __init__(self, colors):
        self.colors = colors
        self.order_button = Button((715, 150), (200, 100), self.colors['blue'])
        self.chaos_button = Button((935, 150), (200, 100), self.colors['blue'])
        self.easy_button = Button((715, 350), (200, 100), self.colors['red'])
        self.hard_button = Button((935, 350), (200, 100), self.colors['red'])
        self.play_button = Button((715, 550), (420, 100), self.colors['gray'])
        self.choosen_level = None
        self.choosen_site = None

    def draw(self, screen):
        white = self.colors['white']
        gray = self.colors['gray']
        blue = self.colors['blue']
        red = self.colors['red']

        screen.fill(self.colors['white'])

        welcome_msg = TextSurface('PORZĄDEK I CHAOS', montserrat_font(40),
                                  (50, 50), blue)
        welcome_msg.draw(screen)

        welcome_msg = TextSurface('Błażej Klepacki', montserrat_font(25),
                                  (50, 620), red)
        welcome_msg.draw(screen)

        site_choice_msg = TextSurface('WYBIERZ STRONĘ', montserrat_font(40),
                                      (730, 50), gray)
        site_choice_msg.draw(screen)

        site_choice_com_msg = TextSurface('(porządek rozpoczyna grę)',
                                          montserrat_font(30), (715, 90), gray)
        site_choice_com_msg.draw(screen)

        level_choice_msg = TextSurface('POZIOM TRUDNOŚCI', montserrat_font(40),
                                       (710, 285), gray)
        level_choice_msg.draw(screen)

        self.order_button.draw(screen)
        order_button_text = TextSurface('PORZĄDEK', montserrat_font(20),
                                        (753, 185), white)
        order_button_text.draw(screen)

        self.chaos_button.draw(screen)
        chaos_but_msg = TextSurface('CHAOS', montserrat_font(20), (995, 185),
                                    white)
        chaos_but_msg.draw(screen)

        self.easy_button.draw(screen)
        easy_but_msg = TextSurface('ŁATWY', montserrat_font(20), (775, 385),
                                   white)
        easy_but_msg.draw(screen)

        self.hard_button.draw(screen)
        hard_but_msg = TextSurface('TRUDNY', montserrat_font(20), (990, 385),
                                   white)
        hard_but_msg.draw(screen)

        self.play_button.draw(screen)
        play_but_msg = TextSurface('GRAJ', montserrat_font(30), (880, 580),
                                   white)
        play_but_msg.draw(screen)

    def starter(self):
        ready_to_play = False
        if self.play_button.isclicked():
            ready_to_play = True
        if self.order_button.isclicked():
            self.choosen_site = 'order'
        if self.chaos_button.isclicked():
            self.choosen_site = 'chaos'
        if self.easy_button.isclicked():
            self.choosen_level = 'easy'
        if self.hard_button.isclicked():
            self.choosen_level = 'hard'
        if self.choosen_level and self.choosen_site and ready_to_play:
            return True
        return False