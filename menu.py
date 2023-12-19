from constants import colors
import pygame
pygame.init()
pygame.font.init()


class TextSurface:
    def __init__(self, msg, size, location, color):
        self.msg = msg
        self.color = color
        self.font = pygame.font.Font('montserrat.ttf', size)
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
        self.play_button = Button((50, 450), (420, 100), colors['gray'])
        self.choosen_level = None
        self.choosen_site = None
        self.before_game = True

    def draw(self, screen):
        screen.fill(colors['white'])

        welcome_msg = TextSurface('PORZĄDEK I CHAOS', 50, (50, 50),
                                  colors['blue'])
        welcome_msg.draw(screen)

        site_info = TextSurface('wybrana strona:', 30, (50, 150),
                                colors['gray'])
        site_info.draw(screen)

        level_info = TextSurface('wybrany poziom:', 30, (50, 250),
                                 colors['gray'])
        level_info.draw(screen)

        easy_expl_msg = 'poziom łatwy: komputer wykonuje losowe ruchy'
        easy_expl = TextSurface(easy_expl_msg, 20, (50, 350), colors['gray'])
        easy_expl.draw(screen)

        hard_expl_msg = 'poziom trudny: komputer gra najlepiej jak umie'
        hard_expl = TextSurface(hard_expl_msg, 20, (50, 380), colors['gray'])
        hard_expl.draw(screen)

        signature = TextSurface('Błażej Klepacki', 25, (50, 620),
                                colors['gray'])
        signature.draw(screen)

        site_choice_msg = TextSurface('WYBIERZ STRONĘ', 40, (730, 50),
                                      colors['gray'])
        site_choice_msg.draw(screen)

        site_choice_com_msg = TextSurface('(porządek rozpoczyna grę)', 30,
                                          (715, 90), colors['gray'])
        site_choice_com_msg.draw(screen)

        level_choice_msg = TextSurface('POZIOM TRUDNOŚCI', 40, (710, 285),
                                       colors['gray'])
        level_choice_msg.draw(screen)

        self.order_button.draw(screen)
        order_button_text = TextSurface('PORZĄDEK', 20, (753, 185),
                                        colors['white'])
        order_button_text.draw(screen)

        self.chaos_button.draw(screen)
        chaos_but_msg = TextSurface('CHAOS', 20, (995, 185), colors['white'])
        chaos_but_msg.draw(screen)

        self.easy_button.draw(screen)
        easy_but_msg = TextSurface('ŁATWY', 20, (775, 385), colors['white'])
        easy_but_msg.draw(screen)

        self.hard_button.draw(screen)
        hard_but_msg = TextSurface('TRUDNY', 20, (990, 385), colors['white'])
        hard_but_msg.draw(screen)

        self.play_button.draw(screen)
        play_but_msg = TextSurface('GRAJ', 30, (200, 480), colors['white'])
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
                order_active_info = TextSurface('PORZĄDEK', 30, (320, 150),
                                                colors['red'])
                order_active_info.draw(screen)
            if self.chaos_button.isclicked():
                pygame.draw.rect(screen, white, (320, 150, 200, 100))
                self.choosen_site = 'chaos'
                chaos_active_info = TextSurface('CHAOS', 30, (320, 150),
                                                colors['blue'])
                chaos_active_info.draw(screen)
            if self.easy_button.isclicked():
                self.choosen_level = 'easy'
                pygame.draw.rect(screen, white, (340, 250, 200, 50))
                easy_active_info = TextSurface('ŁATWY', 30, (340, 250),
                                               colors['red'])
                easy_active_info.draw(screen)
            if self.hard_button.isclicked():
                self.choosen_level = 'hard'
                pygame.draw.rect(screen, white, (330, 250, 200, 50))
                hard_active_info = TextSurface('TRUDNY', 30, (340, 250),
                                               colors['blue'])
                hard_active_info.draw(screen)
        if self.choosen_level and self.choosen_site and ready_to_play:
            return True
        return False

    def ingame(self, screen, site, level):
        white = colors['white']
        pygame.draw.rect(screen, white, (0, 0, 1200, 700))

        if site == 'order':
            site_info = TextSurface('grasz jako porządek', 30, (750, 50),
                                    colors['gray'])
            site_info.draw(screen)
        if site == 'chaos':
            site_info = TextSurface('grasz jako chaos', 30, (750, 50),
                                    colors['gray'])
            site_info.draw(screen)
        if level == 'easy':
            level_info = TextSurface('poziom: łatwy', 30, (750, 100),
                                     colors['gray'])
            level_info.draw(screen)
        if level == 'hard':
            level_info = TextSurface('poziom: trudny', 30, (750, 100),
                                     colors['gray'])
            level_info.draw(screen)
