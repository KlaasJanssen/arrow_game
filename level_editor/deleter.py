import pygame
from settings import vars

class Deleter:
    def __init__(self):
        self.vars = vars

    def detect_click(self, player, enemies, obstacles):
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if player.player:
                if player.player.sprite.rect.collidepoint(mouse_pos):
                    player.player.sprite.kill()
            if enemies.enemies:
                for enemy in enemies.enemies.sprites():
                    if enemy.rect.collidepoint(mouse_pos):
                        enemy.kill()
            if obstacles.obstacles:
                for obstacle in obstacles.obstacles.sprites():
                    if obstacle.rect.collidepoint(mouse_pos):
                        obstacle.kill()


    def update(self, player, enemies, obstacles):
        if self.vars.selected == 'delete':
            self.detect_click(player, enemies, obstacles)
