import pygame
from button import Level_Button
from settings import vars, screen_width
from game_data import levels

class Level_Select:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.vars = vars
        self.total_levels = len(levels)
        #self.total_levels = 15

        self.font = pygame.font.Font(None, 80)
        self.text_surf = self.font.render('Level Select', True, 'White')
        self.text_rect = self.text_surf.get_rect(center = (screen_width / 2, int(175 / 2)))

        self.background = pygame.image.load('../assets/level_select_background.png').convert_alpha()
        self.level_background = pygame.Rect(0,0,self.text_surf.get_size()[0] + 30, self.text_surf.get_size()[1] + 20)
        self.level_background.center = (screen_width / 2, int(175 / 2))


        self.buttons = []
        for i in range(5):
            for j in range(3):
                if not ( i + 1 + j * 5) > self.total_levels:
                    level_button = Level_Button((i * 175 + 200, j * 175 + 225), i + 1 + j * 5)
                    self.buttons.append(level_button)

    def run(self):
        self.screen.blit(self.background, (0,0))
        pygame.draw.rect(self.screen, '#e7c966', self.level_background, 0, 8)
        for button in self.buttons:
            button.draw()
            button.update()
        self.screen.blit(self.text_surf, self.text_rect)
