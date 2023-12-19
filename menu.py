from constants import WHITE, BLUE, RED, GRAY
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
        self.order_button = Button((715, 150), (200, 100), BLUE)
        self.chaos_button = Button((935, 150), (200, 100), BLUE)
        self.easy_button = Button((715, 350), (200, 100), RED)
        self.hard_button = Button((935, 350), (200, 100), RED)
        self.play_button = Button((50, 450), (420, 100), GRAY)
        self.choosen_level = None
        self.choosen_site = None
        self.before_game = True

    def draw(self, screen):
        screen.fill(WHITE)

        welcome_msg = TextSurface('PORZĄDEK I CHAOS', 50, (50, 50), BLUE)
        welcome_msg.draw(screen)

        site_info = TextSurface('wybrana strona:', 30, (50, 150), GRAY)
        site_info.draw(screen)

        level_info = TextSurface('wybrany poziom:', 30, (50, 250), GRAY)
        level_info.draw(screen)

        easy_expl_msg = 'poziom łatwy: komputer wykonuje losowe ruchy'
        easy_expl = TextSurface(easy_expl_msg, 20, (50, 350), GRAY)
        easy_expl.draw(screen)

        hard_expl_msg = 'poziom trudny: komputer gra najlepiej jak umie'
        hard_expl = TextSurface(hard_expl_msg, 20, (50, 380), GRAY)
        hard_expl.draw(screen)

        signature = TextSurface('Błażej Klepacki', 25, (50, 620), GRAY)
        signature.draw(screen)

        site_choice_msg = TextSurface('WYBIERZ STRONĘ', 40, (730, 50), GRAY)
        site_choice_msg.draw(screen)

        shc_msg = TextSurface('(porządek rozpoczyna grę)', 30, (715, 90), GRAY)
        shc_msg.draw(screen)

        lvl_choice_msg = TextSurface('POZIOM TRUDNOŚCI', 40, (710, 285), GRAY)
        lvl_choice_msg.draw(screen)

        self.order_button.draw(screen)
        order_button_text = TextSurface('PORZĄDEK', 20, (753, 185), WHITE)
        order_button_text.draw(screen)

        self.chaos_button.draw(screen)
        chaos_but_msg = TextSurface('CHAOS', 20, (995, 185), WHITE)
        chaos_but_msg.draw(screen)

        self.easy_button.draw(screen)
        easy_but_msg = TextSurface('ŁATWY', 20, (775, 385), WHITE)
        easy_but_msg.draw(screen)

        self.hard_button.draw(screen)
        hard_but_msg = TextSurface('TRUDNY', 20, (990, 385), WHITE)
        hard_but_msg.draw(screen)

        self.play_button.draw(screen)
        play_but_msg = TextSurface('GRAJ', 30, (200, 480), WHITE)
        play_but_msg.draw(screen)

    def starter(self, screen):
        ready_to_play = False
        if self.before_game:
            if self.play_button.isclicked():
                ready_to_play = True
            if self.order_button.isclicked():
                self.choosen_site = 'order'
                pygame.draw.rect(screen, WHITE, (320, 150, 200, 100))
                order_active_inf = TextSurface('PORZĄDEK', 30, (320, 150), RED)
                order_active_inf.draw(screen)
            if self.chaos_button.isclicked():
                pygame.draw.rect(screen, WHITE, (320, 150, 200, 100))
                self.choosen_site = 'chaos'
                chaos_active_info = TextSurface('CHAOS', 30, (320, 150), BLUE)
                chaos_active_info.draw(screen)
            if self.easy_button.isclicked():
                self.choosen_level = 'easy'
                pygame.draw.rect(screen, WHITE, (340, 250, 200, 50))
                easy_active_info = TextSurface('ŁATWY', 30, (340, 250), RED)
                easy_active_info.draw(screen)
            if self.hard_button.isclicked():
                self.choosen_level = 'hard'
                pygame.draw.rect(screen, WHITE, (330, 250, 200, 50))
                hard_active_info = TextSurface('TRUDNY', 30, (340, 250), BLUE)
                hard_active_info.draw(screen)
        if self.choosen_level and self.choosen_site and ready_to_play:
            return True
        return False

    def ingame(self, screen, site, level):
        pygame.draw.rect(screen, WHITE, (0, 0, 1200, 700))

        if site == 'order':
            site_info = TextSurface('grasz jako porządek', 30, (750, 50), GRAY)
            site_info.draw(screen)
        if site == 'chaos':
            site_info = TextSurface('grasz jako chaos', 30, (750, 50), GRAY)
            site_info.draw(screen)
        if level == 'easy':
            level_info = TextSurface('poziom: łatwy', 30, (750, 100), GRAY)
            level_info.draw(screen)
        if level == 'hard':
            level_info = TextSurface('poziom: trudny', 30, (750, 100), GRAY)
            level_info.draw(screen)
