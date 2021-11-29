import pygame
from settings import vars, screen_width, screen_height
from obstacle_object import Obstacle_Object

class Obstacles:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.vars = vars

        self.obstacles = pygame.sprite.Group()
        self.selected = 'none'
        self.remain_clicked = False

    def detect_click(self):
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if not pygame.Rect(screen_width - 300, 0, screen_width, screen_height).collidepoint(mouse_pos):
                if not self.remain_clicked:
                    collided = False
                    for obstacle in self.obstacles.sprites():
                        if obstacle.rect.collidepoint(mouse_pos) and obstacle.type == self.vars.selected:
                            self.selected = obstacle
                            collided = True
                    if not collided:
                        self.selected = Obstacle_Object(mouse_pos, self.vars.selected)
                        self.obstacles.add(self.selected)
                    self.remain_clicked = True
        else:
            self.remain_clicked = False

    def update_pos(self):
        if not self.selected == 'none':
            if not self.selected.change_size:
                mouse_pos = pygame.mouse.get_pos()
                if not pygame.Rect(screen_width - 300, 0, screen_width, screen_height).collidepoint(mouse_pos):
                    if pygame.mouse.get_pressed()[0]:
                        self.selected.rect.center = pygame.mouse.get_pos()
                        if self.selected.rect.right >= screen_width - 300:
                            self.selected.rect.right = screen_width - 300

    def draw(self):
        self.obstacles.draw(self.screen)

    def update(self):
        if self.vars.selected == 'wood' or self.vars.selected == 'metal':
            self.detect_click()
            self.update_pos()
        self.obstacles.update()
