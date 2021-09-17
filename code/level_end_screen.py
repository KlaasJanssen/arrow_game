import pygame
from settings import vars, screen_width, screen_height
from button import Button

class Level_End:
    def __init__(self, type):
        self.screen = pygame.display.get_surface()
        self.type = type
        self.vars = vars
        self.font = pygame.font.Font(None, 60)
        if type == 'won':
            self.end_text = self.font.render('Level Complete!', True, 'White')
        elif type == 'lost':
            self.end_text = self.font.render('Out of Arrows', True, 'White')
        self.end_text_rect = self.end_text.get_rect(center = (screen_width / 2, screen_height / 4 + 80))

        self.background_surf = pygame.image.load('../assets/level_end_menu.png').convert_alpha()
        self.background_rect = self.background_surf.get_rect(center = (screen_width / 2, screen_height / 2))

        self.next_level_button = Button((screen_width * 3/8 + 45, screen_height * 5/8 - 10), 125, 60, 'Next Level', 28, self.vars.start_next_level)
        self.menu_button = Button((screen_width * 5/8 - 45, screen_height * 5/8 - 10), 125, 60, 'Menu', 28, self.vars.change_state_level_select)

        self.countdown = 30

    def draw(self):
        self.countdown -= 1
        if self.countdown <= 0:
            self.screen.blit(self.background_surf, self.background_rect)

            self.screen.blit(self.end_text, self.end_text_rect)

            self.next_level_button.update()
            self.next_level_button.draw()

            self.menu_button.update()
            self.menu_button.draw()
