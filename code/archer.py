import pygame
from arrow import Arrow

class Archer(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # Setup
        self.screen = pygame.display.get_surface()
        self.pos = pos

        self.image = pygame.Surface((40,90))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect(bottomleft = pos)

        # Arrows
        self.arrows = pygame.sprite.Group()
        self.arrow_available = True
        self.max_countdown = 60
        self.arrow_countdown = 0

    def get_input(self):
        if pygame.mouse.get_pressed()[0] and self.arrow_available:
            self.arrows.add(Arrow(self.rect.topright, pygame.math.Vector2(3,-10)))
            self.arrow_countdown = self.max_countdown
            self.arrow_available = False

    def update_countdown(self):
        self.arrow_countdown -= 1
        if self.arrow_countdown <= 0:
            self.arrow_available = True

    def update(self):
        # Updates
        self.get_input()
        self.update_countdown()
        self.arrows.update()

        # Draw
        self.arrows.draw(self.screen)
