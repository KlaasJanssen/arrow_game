import pygame

class Arrow(pygame.sprite.Sprite):
    def __init__(self, pos, velocity):
        super().__init__()
        self.image = pygame.Surface((5,10))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = pos)

        self.pos = pos
        self.velocity = velocity

    def move(self):
        self.pos += self.velocity
        self.rect.center = self.pos

    def apply_gravity(self):
        self.velocity[1] += 0.1

    def update(self):
        self.move()
        self.apply_gravity()
