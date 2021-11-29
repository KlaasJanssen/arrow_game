import pygame
from settings import screen_width, screen_height, vars
from text_input import Text_Input

class Ground:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.vars = vars

        self.ground_height = screen_height

        self.image = pygame.image.load('../assets/ground.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (0, self.ground_height))

        self.text_height = Text_Input((screen_width - 125, screen_height / 2 + 150), 'Height', screen_height, 'height')

    def move_ground(self):
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if not pygame.Rect(screen_width - 300, 0, 300, screen_height).collidepoint(mouse_pos):
                self.rect.top = mouse_pos[1]
                self.ground_height = self.rect.top
                self.update_ground_height()


    def update_text_boxes(self):
        self.ground_height = self.text_height.update(self.ground_height)
        self.update_ground_height()
        self.text_height.draw()

    def update_ground_height(self):
        self.rect.top = self.ground_height
        self.vars.ground_height = self.rect.top

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.vars.selected == 'ground':
            self.move_ground()
            self.update_text_boxes()
