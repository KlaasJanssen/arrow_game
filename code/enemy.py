import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image = pygame.image.load('../assets/enemy.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.bow = pygame.image.load('../assets/enemy_bow.png').convert_alpha()
        self.image.blit(self.bow, (0,0))
        self.rect = self.image.get_rect(bottomleft = pos)

        self.dead = False

    def animate(self):
        if self.dead:
            pass

    def update(self):
        self.animate()
