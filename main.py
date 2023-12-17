import pygame
pygame.init()
pygame.font.init()

# set up constants
screen_size = (1200, 700)
fonts = {40: pygame.font.Font('montserrat.ttf', 40),
         30: pygame.font.Font('montserrat.ttf', 30),
         20: pygame.font.Font('montserrat.ttf', 20)}
colors = {'white': (249, 245, 235),
          'blue': (0, 43, 91),
          'red': (234, 84, 85),
          'gray': (75, 76, 77)
          }

# create screen
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Porządek i chaos')
screen.fill(colors['white'])

# draw board
for line in range(7):
    height = width = line * 100 + 50
    start_coords = (50, height)
    end_coords = (650, height)
    pygame.draw.line(screen, colors['gray'], start_coords, end_coords, 5)
    pygame.draw.line(screen, colors['gray'],
                     (start_coords[1], start_coords[0]),
                     (end_coords[1], end_coords[0]), 5)


# draw text and buttons
class TextSurface:
    def __init__(self, msg, font, location, color=colors['gray']):
        self.msg = msg
        self.font = font
        self.color = color
        self.location = location

    def draw(self):
        surf = self.font.render(self.msg, False, self.color)
        screen.blit(surf, self.location)


site_choice = TextSurface('WYBIERZ STRONĘ', fonts[40], (730, 50))
site_choice.draw()

stch_com = TextSurface('(porządek rozpoczyna grę)', fonts[30], (715, 90))
stch_com.draw()

pygame.draw.rect(screen, colors['blue'], (715, 150, 200, 100))
pygame.draw.rect(screen, colors['blue'], (935, 150, 200, 100))

order_but = TextSurface('PORZĄDEK', fonts[20], (753, 185), colors['white'])
order_but.draw()

chaos_but = TextSurface('CHAOS', fonts[20], (995, 185), colors['white'])
chaos_but.draw()

level_choice = TextSurface('POZIOM TRUDNOŚCI', fonts[40], (710, 300))
level_choice.draw()

pygame.draw.rect(screen, colors['red'], (715, 370, 200, 100))
pygame.draw.rect(screen, colors['red'], (935, 370, 200, 100))



# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
