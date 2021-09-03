import pygame
from settings import vars, screen_width, screen_height
from game_data import levels
from archer import Archer

class Level:
    def __init__(self, current_level):

        # Setup
        self.screen = pygame.display.get_surface()
        self.vars = vars
        self.current_level = current_level
        self.level_data = levels[self.current_level]
        self.player = pygame.sprite.GroupSingle(Archer(self.level_data['player_pos']))
        self.ground_height = self.level_data['ground_height']

        # Create Ground
        self.ground_surf = pygame.Surface((screen_width, screen_height - self.ground_height))
        self.ground_surf.fill((146, 105, 64))
        self.ground_rect = self.ground_surf.get_rect(topleft = (0, self.ground_height))

    def run(self):

        # Update
        self.player.update()

        # Draw
        self.screen.blit(self.ground_surf, self.ground_rect)
        self.player.draw(self.screen)
