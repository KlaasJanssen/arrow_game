import pygame
from support import import_folder

class Particle(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.frames = import_folder('../assets/enemy_blood')
        self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]
        self.rect = self.image.get_rect(center = pos)
        self.animation_speed = 0.25


    def animate(self):
        self.image = self.frames[int(self.frame_index)]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()

    def update(self):
        self.animate()
