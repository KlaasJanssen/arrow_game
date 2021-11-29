import pygame
from settings import vars, screen_width, screen_height
from enemy_object import Enemy_Object

class Enemies:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.vars = vars

        self.enemies = pygame.sprite.Group()
        self.selected = 'none'
        self.remain_clicked = False

    def detect_click(self):
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if not pygame.Rect(screen_width - 300, 0, screen_width, screen_height).collidepoint(mouse_pos):
                if not self.remain_clicked:
                    collided = False
                    for enemy in self.enemies.sprites():
                        if enemy.rect.collidepoint(mouse_pos):
                            self.selected = enemy
                            collided = True
                    if not collided:
                        self.selected = Enemy_Object(mouse_pos)
                        self.enemies.add(self.selected)
                    self.remain_clicked = True
        else:
            self.remain_clicked = False

    def update_pos(self):
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if not pygame.Rect(screen_width - 300, 0, screen_width, screen_height).collidepoint(mouse_pos):
                if not self.selected == 'none':
                    self.selected.rect.center = mouse_pos
                    if self.selected.rect.right > screen_width - 300:
                        self.selected.rect.right = screen_width - 300

    def snapping(self, obstacles):
        if pygame.mouse.get_pressed()[0]:
            if not self.selected == 'none':
                if abs(self.selected.rect.bottom - self.vars.ground_height) < 10:
                    self.selected.rect.bottom = self.vars.ground_height

    def update_text_boxes(self):
        if not self.selected == 'none':
            self.selected.update_text_boxes()

    def draw(self):
        self.enemies.draw(self.screen)

    def update(self, obstacles):
        if self.vars.selected == 'enemy':
            self.detect_click()
            self.update_pos()
            self.snapping(obstacles)
            self.update_text_boxes()
        else:
            self.selected = 'none'
