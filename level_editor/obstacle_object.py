import pygame
from settings import screen_width, screen_height
from text_input import Text_Input

class Obstacle_Object(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        super().__init__()
        self.screen = pygame.display.get_surface()

        self.pos = pos
        self.type = type
        
        self.change_size = True
        self.start = pos

        if self.type == 'wood':
            self.corner = pygame.image.load('../assets/wood_obstacles/wood_corner.png').convert_alpha()
            self.background = pygame.image.load('../assets/wood_obstacles/wood_background.png').convert_alpha()
            self.side = pygame.image.load('../assets/wood_obstacles/wood_side.png').convert_alpha()
        elif self.type == 'metal':
            self.corner = pygame.image.load('../assets/metal_obstacles/metal_corner.png').convert_alpha()
            self.background = pygame.image.load('../assets/metal_obstacles/metal_background.png').convert_alpha()
            self.side = pygame.image.load('../assets/metal_obstacles/metal_side.png').convert_alpha()

        self.create_obstacle_image()


    def create_obstacle_image(self):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] - self.start[0] >= 20 and mouse_pos[1] - self.start[1] >= 20:
            image = pygame.Surface((mouse_pos[0] - self.start[0], mouse_pos[1] - self.start[1]))
            width = image.get_size()[0]
            height = image.get_size()[1]

            # Obstacle background
            background_width = self.background.get_size()[0]
            background_height = self.background.get_size()[0]
            for i in range(int(width / background_width + 1)):
                for j in range(int(height / background_height + 1)):
                    image.blit(self.background, (i * background_width, j * background_height))

            # Sides
            flipped_side = pygame.transform.flip(self.side, True, False)

            for i in range(int(height / 10 + 1)):
                image.blit(self.side, (0,i*10))
                image.blit(flipped_side, (width - 10, i*10))

            horizontal_side = pygame.transform.rotate(self.side, -90)
            horizontal_side_flipped = pygame.transform.flip(horizontal_side, False, True)

            for i in range(int(width / 10 + 1)):
                image.blit(horizontal_side, (i*10, 0))
                image.blit(horizontal_side_flipped, (i*10, height - 10))

            # Corners
            corner_90 = pygame.transform.rotate(self.corner, 90)
            corner_180 = pygame.transform.rotate(self.corner, 180)
            corner_270 = pygame.transform.rotate(self.corner, 270)

            image.blit(self.corner, (0,0))
            image.blit(corner_90, (0,height - 10))
            image.blit(corner_180, (width - 10,height - 10))
            image.blit(corner_270, (width - 10,0))

            self.image = image
            self.rect = self.image.get_rect(topleft = self.start)
        else:
            self.image = pygame.Surface((0,0))
            self.rect = self.image.get_rect(topleft = self.start)

    def update_size(self):
        if self.change_size:
            self.create_obstacle_image()
            if not pygame.mouse.get_pressed()[0]:
                self.change_size = False
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] - self.start[0] < 20 or mouse_pos[1] - self.start[1] < 20:
                    self.kill()

    def update(self):
        self.update_size()
