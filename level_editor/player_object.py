import pygame
from settings import screen_width, screen_height

class Player_Object(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('../assets/editor/archer.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)
