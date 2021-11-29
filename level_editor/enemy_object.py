import pygame
from text_input import Text_Input
from settings import screen_width, screen_height

class Enemy_Object(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.screen = pygame.display.get_surface()

        self.image = pygame.image.load('../assets/editor/enemy.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)

        self.text_left = Text_Input((screen_width - 125, screen_height / 2 + 150), 'Left', 0, 'width')
        self.text_bottom = Text_Input((screen_width - 125, screen_height / 2 + 200), 'Bottom', 0, 'height')

    def highlight(self):
        pygame.draw.Rect(self.screen, (255,255,255), self.rect, 3)

    def update_text_boxes(self):
        self.rect.bottom = self.text_bottom.update(self.rect.bottom)
        self.rect.left = self.text_left.update(self.rect.left)

        self.text_bottom.draw()
        self.text_left.draw()
