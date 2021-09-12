import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, data):
        super().__init__()
        self.left = data[0]
        self.top = data[1]
        self.right = data[2]
        self.bottom = data[3]

        self.image = pygame.Surface((self.right - self.left, self.bottom - self.top))
        self.image.fill((146, 105, 64))
        self.rect = self.image.get_rect(topleft = (self.left, self.top))
