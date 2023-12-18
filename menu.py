from constants import montserrat_font, colors
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
    def __init__(self):
        self.order_button = Button((715, 150), (200, 100), colors['blue'])
        self.chaos_button = Button((935, 150), (200, 100), colors['blue'])
        self.easy_button = Button((715, 350), (200, 100), colors['red'])
        self.hard_button = Button((935, 350), (200, 100), colors['red'])
        self.play_button = Button((715, 550), (420, 100), colors['gray'])
        self.x_button = Button((750, 475), (150, 150), colors['red'])
        self.o_button = Button((950, 475), (150, 150), colors['blue'])
        self.choosen_level = None
        self.choosen_site = None
        self.before_game = True

    def draw(self, screen):
        screen.fill(colors['white'])

        welcome_msg = TextSurface('PORZĄDEK I CHAOS', montserrat_font(50),
                                  (50, 50), colors['blue'])
        welcome_msg.draw(screen)

        site_info = TextSurface('wybrana strona:', montserrat_font(30),
                                (50, 150), colors['gray'])
        site_info.draw(screen)

        level_info = TextSurface('wybrana poziom:', montserrat_font(30),
                                 (50, 250), colors['gray'])
        level_info.draw(screen)

        easy_expl_msg = 'poziom łatwy: komputer wykonuje losowe ruchy'
        easy_expl = TextSurface(easy_expl_msg, montserrat_font(20),
                                (50, 350), colors['gray'])
        easy_expl.draw(screen)

        hard_expl_msg = 'poziom trudny: komputer gra najlepiej jak umie'
        hard_expl = TextSurface(hard_expl_msg, montserrat_font(20),
                                (50, 380), colors['gray'])
        hard_expl.draw(screen)

        signature = TextSurface('Błażej Klepacki', montserrat_font(25),
                                (50, 620), colors['gray'])
        signature.draw(screen)

        site_choice_msg = TextSurface('WYBIERZ STRONĘ', montserrat_font(40),
                                      (730, 50), colors['gray'])
        site_choice_msg.draw(screen)

        site_choice_com_msg = TextSurface('(porządek rozpoczyna grę)',
                                          montserrat_font(30), (715, 90),
                                          colors['gray'])
        site_choice_com_msg.draw(screen)

        level_choice_msg = TextSurface('POZIOM TRUDNOŚCI', montserrat_font(40),
                                       (710, 285), colors['gray'])
        level_choice_msg.draw(screen)

        self.order_button.draw(screen)
        order_button_text = TextSurface('PORZĄDEK', montserrat_font(20),
                                        (753, 185), colors['white'])
        order_button_text.draw(screen)

        self.chaos_button.draw(screen)
        chaos_but_msg = TextSurface('CHAOS', montserrat_font(20), (995, 185),
                                    colors['white'])
        chaos_but_msg.draw(screen)

        self.easy_button.draw(screen)
        easy_but_msg = TextSurface('ŁATWY', montserrat_font(20), (775, 385),
                                   colors['white'])
        easy_but_msg.draw(screen)

        self.hard_button.draw(screen)
        hard_but_msg = TextSurface('TRUDNY', montserrat_font(20), (990, 385),
                                   colors['white'])
        hard_but_msg.draw(screen)

        self.play_button.draw(screen)
        play_but_msg = TextSurface('GRAJ', montserrat_font(30), (880, 580),
                                   colors['white'])
        play_but_msg.draw(screen)

    def starter(self, screen):
        white = colors['white']
        ready_to_play = False
        if self.before_game:
            if self.play_button.isclicked():
                ready_to_play = True
            if self.order_button.isclicked():
                self.choosen_site = 'order'
                pygame.draw.rect(screen, white, (320, 150, 200, 100))
                order_active_info = TextSurface('PORZĄDEK',
                                                montserrat_font(30),
                                                (320, 150), colors['red'])
                order_active_info.draw(screen)
            if self.chaos_button.isclicked():
                pygame.draw.rect(screen, white, (320, 150, 200, 100))
                self.choosen_site = 'chaos'
                chaos_active_info = TextSurface('CHAOS',
                                                montserrat_font(30),
                                                (320, 150),
                                                colors['blue'])
                chaos_active_info.draw(screen)
            if self.easy_button.isclicked():
                self.choosen_level = 'easy'
                pygame.draw.rect(screen, white, (340, 250, 200, 50))
                easy_active_info = TextSurface('ŁATWY',
                                               montserrat_font(30), (340, 250),
                                               colors['red'])
                easy_active_info.draw(screen)
            if self.hard_button.isclicked():
                self.choosen_level = 'hard'
                pygame.draw.rect(screen, white, (330, 250, 200, 50))
                hard_active_info = TextSurface('TRUDNY',
                                               montserrat_font(30), (340, 250),
                                               colors['blue'])
                hard_active_info.draw(screen)
        if self.choosen_level and self.choosen_site and ready_to_play:
            return True
        return False

    def ingame(self, screen, site, level):
        white = colors['white']
        pygame.draw.rect(screen, white, (0, 0, 1200, 700))

        if site == 'order':
            site_info = TextSurface('grasz jako porządek', montserrat_font(30),
                                    (750, 50), colors['gray'])
            site_info.draw(screen)
        if site == 'chaos':
            site_info = TextSurface('grasz jako chaos', montserrat_font(30),
                                    (750, 50), colors['gray'])
            site_info.draw(screen)
        if level == 'easy':
            level_info = TextSurface('poziom: łatwy', montserrat_font(30),
                                     (750, 100), colors['gray'])
            level_info.draw(screen)
        if level == 'hard':
            level_info = TextSurface('poziom: trudny', montserrat_font(30),
                                     (750, 100), colors['gray'])
            level_info.draw(screen)

        self.x_button.draw(screen)
        self.o_button.draw(screen)
        x_but_msg = TextSurface('X', montserrat_font(130), (775, 472), white)
        x_but_msg.draw(screen)
        o_but_msg = TextSurface('O', montserrat_font(130), (970, 470), white)
        o_but_msg.draw(screen)
