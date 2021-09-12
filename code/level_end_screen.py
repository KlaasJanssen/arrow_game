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
            self.end_text = self.font.render('Level Complete!', True, 'Black')
        elif type == 'lost':
            self.end_text = self.font.render('Out of Arrows', True, 'Black')
        self.end_text_rect = self.end_text.get_rect(center = (screen_width / 2, screen_height / 4 + 50))

        self.background_surf = pygame.Surface((screen_width / 2, screen_height / 2))
        self.background_rect = self.background_surf.get_rect(center = (screen_width / 2, screen_height / 2))

        self.next_level_button = Button((screen_width * 3/8, screen_height * 5/8), screen_width * 8/48, 75, 'Next Level', 40, self.vars.start_next_level)
        self.menu_button = Button((screen_width * 5/8, screen_height * 5/8), screen_width * 8/48, 75, 'Menu', 40)

    def draw(self):
        pygame.draw.rect(self.screen, (210,210,210), self.background_rect, 0, 15)
        pygame.draw.rect(self.screen, (50,50,50), self.background_rect, 4, 15)

        self.screen.blit(self.end_text, self.end_text_rect)

        self.next_level_button.update()
        self.next_level_button.draw()

        self.menu_button.update()
        self.menu_button.draw()
