import pygame
from support import import_folder

class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, obstacle = None):
        super().__init__()
        self.frames = import_folder('../assets/enemy_blood')
        self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]
        self.rect = self.image.get_rect(center = pos)
        self.animation_speed = 0.25

        self.obstacle = obstacle

        if self.obstacle:
            self.offset = pygame.math.Vector2(self.rect.topleft) - pygame.math.Vector2(self.obstacle.rect.topleft)


    def animate(self):
        self.image = self.frames[int(self.frame_index)]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()

    def move(self):
        if self.obstacle:
            self.rect.topleft = self.obstacle.rect.topleft + self.offset

    def update(self):
        self.animate()
        self.move()
