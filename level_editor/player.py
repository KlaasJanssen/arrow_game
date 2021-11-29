import pygame
from settings import screen_width, screen_height, vars
from player_object import Player_Object
from text_input import Text_Input

class Player:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.vars = vars

        self.player = pygame.sprite.GroupSingle()

        self.text_left = Text_Input((screen_width - 125, screen_height / 2 + 150), 'Left', 0, 'width')
        self.text_bottom = Text_Input((screen_width - 125, screen_height / 2 + 200), 'Bottom', 0, 'height')

    def detect_click(self):
        if self.vars.selected == 'player':
            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                if pygame.Rect(screen_width - 300, 0, 300, screen_height).collidepoint(mouse_pos):
                    return
                if not self.player:
                    self.player.add(Player_Object(mouse_pos))
                else:
                    self.player.sprite.rect.center = mouse_pos

    def snapping(self, obstacles):
        if pygame.mouse.get_pressed()[0]:
            if self.player:
                player_rect = self.player.sprite.rect
                if abs(player_rect.bottom - self.vars.ground_height) < 10:
                    player_rect.bottom = self.vars.ground_height

    def update_text_boxes(self):
        if self.player:
            player_rect = self.player.sprite.rect
            player_rect.bottom = self.text_bottom.update(player_rect.bottom)
            player_rect.left = self.text_left.update(player_rect.left)

            self.text_bottom.draw()
            self.text_left.draw()

    def draw(self):
        self.player.draw(self.screen)

    def update(self, obstacles):
        if self.vars.selected == 'player':
            self.detect_click()
            self.snapping(obstacles)
            self.update_text_boxes()
