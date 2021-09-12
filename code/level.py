import pygame
from settings import vars, screen_width, screen_height
from game_data import levels
from archer import Archer
from enemy import Enemy
from particles import Particle
from obstacles import Obstacle
from level_end_screen import Level_End

class Level:
    def __init__(self, current_level):

        # Setup
        self.screen = pygame.display.get_surface()
        self.vars = vars
        self.current_level = current_level
        self.level_data = levels[self.current_level]
        self.player = pygame.sprite.GroupSingle(Archer(self.level_data['player_pos'], self.current_level, self.blood_particles))
        self.ground_height = self.level_data['ground_height']
        self.state = 'active'

        # Create Ground
        self.ground_surf = pygame.Surface((screen_width, screen_height - self.ground_height))
        self.ground_surf.fill((146, 105, 64))
        self.ground_rect = self.ground_surf.get_rect(topleft = (0, self.ground_height))

        # Enemies
        self.enemy_data = self.level_data['enemies']
        self.enemies = pygame.sprite.Group()
        for enemy_pos in self.enemy_data:
            self.enemies.add(Enemy(enemy_pos))

        # Blood particles
        self.blood_particles = pygame.sprite.Group()

        # Obstacles
        self.obstacle_data = self.level_data['obstacles']
        self.obstacles = pygame.sprite.Group()
        for obstacle_pos in self.obstacle_data:
            self.obstacles.add(Obstacle(obstacle_pos))

    def blood_particles(self, enemy):
        self.blood_particles.add(Particle(enemy.rect.center))

    def detect_win(self):
        if not self.enemies:
            self.state = 'won'
            self.level_end = Level_End('won')

    def run(self):

        # Update
        if self.state == 'active':
            self.player.update(self.enemies, self.obstacles)
            self.enemies.update()
            self.detect_win()
        self.blood_particles.update()

        # Draw
        # Arrows keep updating and being drawn after game is over
        if not self.state == 'active':
            self.player.sprite.arrows.update(self.enemies, self.obstacles)
            self.player.sprite.arrows.draw(self.screen)

        # General drawing
        self.screen.blit(self.ground_surf, self.ground_rect)
        self.enemies.draw(self.screen)
        self.player.draw(self.screen)
        self.blood_particles.draw(self.screen)
        self.obstacles.draw(self.screen)

        # End screen
        if not self.state == 'active':
            self.player.sprite.draw_bow()
            #self.level_end.draw()
