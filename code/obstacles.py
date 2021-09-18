import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, data):
        super().__init__()
        self.left = data[0]
        self.top = data[1]
        self.right = data[2]
        self.bottom = data[3]
        self.material = data[4]
        self.type = data[5] # static or dynamic

        if self.type == 'dynamic':
            self.movement_type = data[6] # horizontal or vertical
            self.direction = 1
            if self.movement_type == 'horizontal':
                self.left_bound = data[7]
                self.right_bound = data[8]
            else:
                self.upper_bound = data[7]
                self.lower_bound = data[8]
            self.speed = data[9]

        self.image = pygame.Surface((self.right - self.left, self.bottom - self.top))
        if self.material == 'wood':
            self.image.fill((146, 105, 64))
        elif self.material == 'metal':
            self.image.fill((150,150,150))
        self.rect = self.image.get_rect(topleft = (self.left, self.top))

    def move(self):
        if self.type == 'dynamic':
            if self.movement_type == 'horizontal':
                self.rect.x += self.speed * self.direction
                if self.rect.left <= self.left_bound:
                    self.rect.left = self.left_bound
                    self.direction *= -1
                elif self.rect.right >= self.right_bound:
                    self.rect.right = self.right_bound
                    self.direction *= -1
            else:
                self.rect.y += self.speed * self.direction
                if self.rect.top <= self.upper_bound:
                    self.rect.top = self.upper_bound
                    self.direction *= -1
                elif self.rect.bottom >= self.lower_bound:
                    self.rect.bottom = self.lower_bound
                    self.direction *= -1

    def update(self):
        self.move()
