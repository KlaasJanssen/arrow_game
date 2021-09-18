import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, obstacles):
        super().__init__()
        self.pos = pos
        self.image = pygame.image.load('../assets/enemy.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.bow = pygame.image.load('../assets/enemy_bow.png').convert_alpha()
        self.image.blit(self.bow, (0,0))
        self.rect = self.image.get_rect(bottomleft = pos)

        self.dead = False
        self.moving = False

        # detect if on moving obstacle
        moving_detect_rect = pygame.Rect(self.rect.left, self.rect.bottom, self.image.get_size()[0], 10)
        for obstacle in obstacles.sprites():
            if moving_detect_rect.colliderect(obstacle.rect):
                if obstacle.type == 'dynamic':
                    self.moving = True
                    self.moving_on = obstacle
                    self.offset = pygame.math.Vector2(self.rect.topleft) - pygame.math.Vector2(obstacle.rect.topleft)

    def animate(self):
        if self.dead:
            pass

    def move(self):
        if self.moving:
            self.rect.topleft = self.moving_on.rect.topleft + self.offset

    def update(self):
        self.animate()
        self.move()
