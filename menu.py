from colors import white, blue, red, gray
import pygame


def write_text(msg, size, location, color, screen):
    font = pygame.font.Font('montserrat.ttf', size)
    surface = font.render(msg, False, color)
    screen.blit(surface, location)


class Button():
    def __init__(self, coords, size, color):
        self.coords = coords
        self.size = size
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.coords[0], self.coords[1],
                                              self.size[0], self.size[1]))

    def isclicked(self):
        if pygame.mouse.get_pressed()[0] == 1:
            pos = pygame.mouse.get_pos()
            start_x = self.coords[0]
            end_x = self.coords[0] + self.size[0]
            start_y = self.coords[1]
            end_y = self.coords[1] + self.size[1]
            if pos[0] >= start_x and pos[0] <= end_x:
                if pos[1] >= start_y and pos[1] < end_y:
                    return True
        return False


class Menu():
    def __init__(self, screen):
        self.screen = screen
        self.order_button = Button((715, 150), (200, 100), blue)
        self.chaos_button = Button((935, 150), (200, 100), blue)
        self.easy_button = Button((715, 350), (200, 100), red)
        self.hard_button = Button((935, 350), (200, 100), red)
        self.play_button = Button((50, 450), (420, 100), gray)
        self.choosen_level = None
        self.choosen_site = None
        self.before_game = True

    def draw(self):
        self.screen.fill(white)
        self.order_button.draw(self.screen)
        self.chaos_button.draw(self.screen)
        self.easy_button.draw(self.screen)
        self.hard_button.draw(self.screen)
        self.play_button.draw(self.screen)
        write_text('PORZĄDEK I CHAOS', 50, (50, 50), blue, self.screen)
        write_text('wybrana strona:', 30, (50, 150), gray, self.screen)
        write_text('wybrany poziom:', 30, (50, 250), gray, self.screen)
        easy_expl_msg = 'poziom łatwy: komputer wykonuje losowe ruchy'
        write_text(easy_expl_msg, 20, (50, 350), gray, self.screen)
        hard_expl_msg = 'poziom trudny: komputer gra najlepiej jak umie'
        write_text(hard_expl_msg, 20, (50, 380), gray, self.screen)
        write_text('Błażej Klepacki', 25, (50, 620), gray, self.screen)
        write_text('WYBIERZ STRONĘ', 40, (730, 50), gray, self.screen)
        order_starts_msg = '(porządek rozpoczyna grę)'
        write_text(order_starts_msg, 30, (715, 90), gray, self.screen)
        write_text('POZIOM TRUDNOŚCI', 40, (710, 285), gray, self.screen)
        write_text('PORZĄDEK', 20, (753, 185), white, self.screen)
        write_text('CHAOS', 20, (995, 185), white, self.screen)
        write_text('ŁATWY', 20, (775, 385), white, self.screen)
        write_text('TRUDNY', 20, (990, 385), white, self.screen)
        write_text('GRAJ', 30, (200, 480), white, self.screen)

    def starter(self):
        ready_to_play = False
        if self.before_game:
            if self.play_button.isclicked():
                ready_to_play = True
            if self.order_button.isclicked():
                self.choosen_site = 'order'
                pygame.draw.rect(self.screen, white, (320, 150, 200, 100))
                write_text('PORZĄDEK', 30, (320, 150), red, self.screen)
            if self.chaos_button.isclicked():
                pygame.draw.rect(self.screen, white, (320, 150, 200, 100))
                self.choosen_site = 'chaos'
                write_text('CHAOS', 30, (320, 150), blue, self.screen)
            if self.easy_button.isclicked():
                self.choosen_level = 'easy'
                pygame.draw.rect(self.screen, white, (340, 250, 200, 50))
                write_text('ŁATWY', 30, (340, 250), red, self.screen)
            if self.hard_button.isclicked():
                self.choosen_level = 'hard'
                pygame.draw.rect(self.screen, white, (330, 250, 200, 50))
                write_text('TRUDNY', 30, (340, 250), blue, self.screen)
        if self.choosen_level and self.choosen_site and ready_to_play:
            return True
        return False

    def ingame(self, site, level):
        pygame.draw.rect(self.screen, white, (0, 0, 1200, 700))
        map_site = {'order': 'porządek', 'chaos': 'chaos'}
        map_level = {'easy': 'łatwy', 'hard': 'trudny'}
        scr = self.screen
        write_text(f'grasz jako {map_site[site]}', 30, (750, 50), gray, scr)
        write_text(f'poziom: {map_level[level]}', 30, (750, 100), gray, scr)
