import pygame
from settings import vars, screen_width, screen_height

class Button():
    def __init__(self, pos, type):
        self.screen = pygame.display.get_surface()
        self.pos = pos
        self.type = type

        self.vars = vars

        self.image = pygame.Surface((100,100))
        self.rect = self.image.get_rect(topleft = pos)
        self.border_color = (100,100,100)

        self.selected = False

        if self.type == 'ground':
            img = pygame.image.load('../assets/ground.png').convert_alpha()
            img_surface = pygame.Surface((70,70))
            img_surface.blit(img, (0,0))
            img_rect = img_surface.get_rect(center = (50,50))
            self.image.blit(img_surface, img_rect)
        elif self.type == 'wood':
            corner = pygame.image.load('../assets/wood_obstacles/wood_corner.png').convert_alpha()
            background = pygame.image.load('../assets/wood_obstacles/wood_background.png').convert_alpha()
            side = pygame.image.load('../assets/wood_obstacles/wood_side.png').convert_alpha()
            self.create_obstacle_image(background, side, corner)
        elif self.type == 'metal':
            corner = pygame.image.load('../assets/metal_obstacles/metal_corner.png').convert_alpha()
            background = pygame.image.load('../assets/metal_obstacles/metal_background.png').convert_alpha()
            side = pygame.image.load('../assets/metal_obstacles/metal_side.png').convert_alpha()
            self.create_obstacle_image(background, side, corner)
        elif self.type == 'player':
            img = pygame.image.load('../assets/editor/archer.png').convert_alpha()
            img_rect = img.get_rect(center = (50,50))
            self.image.fill((50,50,50))
            self.image.blit(img, img_rect)
        elif self.type == 'enemy':
            img = pygame.image.load('../assets/editor/enemy.png').convert_alpha()
            img_rect = img.get_rect(center = (50,50))
            self.image.fill((50,50,50))
            self.image.blit(img, img_rect)
        elif self.type == 'delete':
            img = pygame.image.load('../assets/editor/garbage_can.png').convert_alpha()
            img_rect = img.get_rect(center = (50,50))
            self.image.fill((50,50,50))
            self.image.blit(img, img_rect)


    def create_obstacle_image(self, background, side, corner):
        image = pygame.Surface((70, 70))
        width = image.get_size()[0]
        height = image.get_size()[1]

        # Obstacle background
        background_width = background.get_size()[0]
        for i in range(int(width / background_width + 1)):
            image.blit(background, (i * background_width,0))

        # Sides
        flipped_side = pygame.transform.flip(side, True, False)

        for i in range(int(height / 10 + 1)):
            image.blit(side, (0,i*10))
            image.blit(flipped_side, (width - 10, i*10))

        horizontal_side = pygame.transform.rotate(side, -90)
        horizontal_side_flipped = pygame.transform.flip(horizontal_side, False, True)

        for i in range(int(width / 10 + 1)):
            image.blit(horizontal_side, (i*10, 0))
            image.blit(horizontal_side_flipped, (i*10, height - 10))

        # Corners
        corner_90 = pygame.transform.rotate(corner, 90)
        corner_180 = pygame.transform.rotate(corner, 180)
        corner_270 = pygame.transform.rotate(corner, 270)

        image.blit(corner, (0,0))
        image.blit(corner_90, (0,height - 10))
        image.blit(corner_180, (width - 10,height - 10))
        image.blit(corner_270, (width - 10,0))

        rect = image.get_rect(center = (50,50))

        self.image.blit(image, rect)

    def detect_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.selected = True
                self.vars.selected = self.type
        elif pygame.Rect(screen_width - 300, 0, 300, screen_height / 2 + 80).collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.selected = False
                if self.vars.selected == self.type:
                    self.vars.selected = 'None'

    def draw(self):
        if self.selected:
            self.border_color = (255,255,255)
        else:
            self.border_color = (100,100,100)

        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, self.border_color, self.rect, 3)

    def update(self):
        self.detect_click()
