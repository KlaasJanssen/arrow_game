import pygame
from arrow import Arrow
from math import atan2, degrees

class Archer(pygame.sprite.Sprite):
    def __init__(self, pos, current_level):
        super().__init__()

        # Setup
        self.screen = pygame.display.get_surface()
        self.pos = pos
        self.current_level = current_level

        self.image = pygame.Surface((40,90))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect(bottomleft = pos)

        # Arrows
        self.arrows = pygame.sprite.Group()
        self.arrow_available = True
        self.max_countdown = 60
        self.arrow_countdown = 0

        # Bow
        self.direction = pygame.math.Vector2(0,0)
        self.angle = 0
        self.power = 0
        self.bow_drawn = False

    def get_input(self):
        self.get_direction()
        if pygame.mouse.get_pressed()[0]:
            if self.arrow_available:
                self.bow_drawn = True
                self.power += 0.2
                if self.power > 15: self.power = 15
        elif self.bow_drawn:
            if self.power >= 1:
                self.arrows.add(Arrow(self.rect.topright, pygame.math.Vector2(self.direction * self.power), self.current_level))
                self.arrow_countdown = self.max_countdown
                self.arrow_available = False
            self.bow_drawn = False
            self.power = 0

    def update_countdown(self):
        self.arrow_countdown -= 1
        if self.arrow_countdown <= 0:
            self.arrow_available = True

    def get_direction(self):
        mouse_pos = pygame.mouse.get_pos()
        self.direction = pygame.math.Vector2(mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery).normalize()
        self.angle = degrees(atan2(self.direction[0], self.direction[1]))

    def show_arrow_path(self):
        if self.arrow_available:
            power = self.power
            if power < 2: power = 2
            pos = self.rect.topright
            velocity = power * self.direction
            radius = 10
            radiusminus = 0
            for i in range(101):
                pos += velocity
                velocity[1] += 0.1
                if i % 5 == 0 and not i == 0:
                    pygame.draw.circle(self.screen, (255,255,255), pos, radius)
                    radiusminus += 1
                    if radiusminus % 2 == 1:
                        radius -= 1

    def update(self):
        # Updates
        self.get_input()
        self.update_countdown()
        self.arrows.update()

        # Draw
        self.arrows.draw(self.screen)
        self.show_arrow_path()
