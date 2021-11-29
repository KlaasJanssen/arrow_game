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
            self.corner = pygame.image.load('../assets/wood_obstacles/wood_corner.png').convert_alpha()
            self.background = pygame.image.load('../assets/wood_obstacles/wood_background.png').convert_alpha()
            self.side = pygame.image.load('../assets/wood_obstacles/wood_side.png').convert_alpha()
            self.create_image()
        elif self.material == 'metal':
            self.corner = pygame.image.load('../assets/metal_obstacles/metal_corner.png').convert_alpha()
            self.background = pygame.image.load('../assets/metal_obstacles/metal_background.png').convert_alpha()
            self.side = pygame.image.load('../assets/metal_obstacles/metal_side.png').convert_alpha()
            self.create_image()
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

    def create_image(self):
        width = self.image.get_size()[0]
        height = self.image.get_size()[1]

        # Obstacle background
        background_width = self.background.get_size()[0]
        for i in range(int(width / background_width + 1)):
            self.image.blit(self.background, (i * background_width,0))

        # Sides
        flipped_side = pygame.transform.flip(self.side, True, False)

        for i in range(int(height / 10 + 1)):
            self.image.blit(self.side, (0,i*10))
            self.image.blit(flipped_side, (width - 10, i*10))

        horizontal_side = pygame.transform.rotate(self.side, -90)
        horizontal_side_flipped = pygame.transform.flip(horizontal_side, False, True)

        for i in range(int(width / 10 + 1)):
            self.image.blit(horizontal_side, (i*10, 0))
            self.image.blit(horizontal_side_flipped, (i*10, height - 10))

        # Corners
        corner_90 = pygame.transform.rotate(self.corner, 90)
        corner_180 = pygame.transform.rotate(self.corner, 180)
        corner_270 = pygame.transform.rotate(self.corner, 270)

        self.image.blit(self.corner, (0,0))
        self.image.blit(corner_90, (0,height - 10))
        self.image.blit(corner_180, (width - 10,height - 10))
        self.image.blit(corner_270, (width - 10,0))


    def update(self):
        self.move()
