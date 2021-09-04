import pygame
from math import atan2, degrees
from game_data import levels

class Arrow(pygame.sprite.Sprite):
    def __init__(self, pos, velocity, current_level):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.image = pygame.Surface((5,10), pygame.SRCALPHA)
        #self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = pos)
        self.arrow_surf = pygame.image.load('../assets/arrow.png').convert_alpha()

        self.current_level = current_level
        self.ground_height = levels[self.current_level]['ground_height']

        self.pos = pos
        self.velocity = velocity
        self.stuck = False

    def move(self):
        self.pos += self.velocity
        self.rect.center = self.pos
        self.detect_collision()

    def detect_collision(self):
        if self.rect.bottom >= self.ground_height:
            self.stuck = True
            self.velocity = pygame.math.Vector2(0,0)

    def apply_gravity(self):
        if not self.stuck:
            self.velocity[1] += 0.1

    def draw_arrow(self):
        if not self.stuck:
            self.rotate_arrow()
        if self.velocity[0] >= 0:
            if self.velocity[1] >= 0:
                self.arrow_rect = self.rotated_arrow.get_rect(bottomright = (self.rect.bottomright[0], self.rect.bottomright[1] + 4))
            else:
                self.arrow_rect = self.rotated_arrow.get_rect(topright = (self.rect.topright[0], self.rect.topright[1] + 4))
        else:
            if self.velocity[1] >= 0:
                self.arrow_rect = self.rotated_arrow.get_rect(bottomleft = (self.rect.bottomleft[0], self.rect.bottomleft[1]))
            else:
                self.arrow_rect = self.rotated_arrow.get_rect(topleft = (self.rect.topleft[0], self.rect.topleft[1]))
        self.screen.blit(self.rotated_arrow, self.arrow_rect)

    def rotate_arrow(self):
        angle = degrees(atan2(self.velocity[0], self.velocity[1])) - 90
        self.rotated_arrow = pygame.transform.rotate(self.arrow_surf, angle)


    def update(self):
        self.move()
        self.apply_gravity()

        self.draw_arrow()
