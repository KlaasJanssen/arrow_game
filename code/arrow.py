import pygame
from math import atan2, degrees
from game_data import levels


class Arrow(pygame.sprite.Sprite):
    def __init__(self, pos, velocity, current_level, blood_particles):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.image = pygame.Surface((5,10), pygame.SRCALPHA)
        #self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = pos)
        self.arrow_surf = pygame.image.load('../assets/arrow.png').convert_alpha()

        self.current_level = current_level
        self.ground_height = levels[self.current_level]['ground_height']

        self.pos = pos
        self.velocity = velocity
        self.stuck = False
        self.stuck_in_moving = False
        self.going_up = False
        self.going_left = False

        self.blood_particles = blood_particles

    def move(self):
        self.pos += self.velocity
        self.rect.center = self.pos
        if self.stuck_in_moving:
            self.rect.topleft = self.stuck_in_obstacle.rect.topleft + self.offset

    def detect_collision(self, enemies, obstacles):
        if self.stuck:
            return

        # Ground
        if self.rect.bottom > self.ground_height:
            self.stuck = True
            if self.velocity[0] < 0:
                self.going_left = True
            self.velocity = pygame.math.Vector2(0,0)

        # Enemy
        for enemy in enemies.sprites():
            if self.rect.colliderect(enemy.rect):
                offset_x = int(self.arrow_rect.left - enemy.rect.left)
                offset_y = int(enemy.rect.top - self.arrow_rect.top)
                offset = (offset_x, offset_y)
                self.arrow_mask = pygame.mask.from_surface(self.rotated_arrow)
                if self.arrow_mask.overlap(enemy.mask, offset):
                    self.stuck = True
                    self.velocity = pygame.math.Vector2(0,0)
                    if not enemy.dead:
                        if enemy.moving:
                            self.blood_particles(enemy, enemy.moving_on)
                        else:
                            self.blood_particles(enemy)
                        enemy.kill()
                        self.kill()

        # Obstacle
        for obstacle in obstacles.sprites():
            if self.rect.colliderect(obstacle.rect):
                if obstacle.material == 'wood':
                    self.stuck = True
                    if self.velocity[0] < 0:
                        self.going_left = True
                    if self.velocity[1] < 0:
                        self.going_up = True
                    self.velocity = pygame.math.Vector2(0,0)
                    if obstacle.type == 'dynamic':
                        self.stuck_in_moving = True
                        self.stuck_in_obstacle = obstacle
                        self.offset = pygame.math.Vector2(self.rect.topleft) - pygame.math.Vector2(obstacle.rect.topleft)
                elif obstacle.material == 'metal':
                    self.velocity[0] *= -1
                    return

    def apply_gravity(self):
        if not self.stuck:
            self.velocity[1] += 0.1

    def get_rotated_arrow_image(self):
        if not self.stuck:
            self.rotate_arrow()
        if self.velocity[0] >= 0 and not self.going_left:
            if self.velocity[1] >= 0 and not self.going_up:
                self.arrow_rect = self.rotated_arrow.get_rect(bottomright = (self.rect.bottomright[0], self.rect.bottomright[1]))
            else:
                self.arrow_rect = self.rotated_arrow.get_rect(topright = (self.rect.topright[0], self.rect.topright[1]))
        else:
            if self.velocity[1] >= 0 and not self.going_up:
                self.arrow_rect = self.rotated_arrow.get_rect(bottomleft = (self.rect.bottomleft[0], self.rect.bottomleft[1]))
            else:
                self.arrow_rect = self.rotated_arrow.get_rect(topleft = (self.rect.topleft[0], self.rect.topleft[1]))

    def draw_arrow(self):
        self.screen.blit(self.rotated_arrow, self.arrow_rect)

    def rotate_arrow(self):
        angle = degrees(atan2(self.velocity[0], self.velocity[1])) - 90
        self.rotated_arrow = pygame.transform.rotozoom(self.arrow_surf, angle, 1)


    def update(self, enemies, obstacles):
        self.move()
        self.get_rotated_arrow_image()
        self.detect_collision(enemies, obstacles)
        self.apply_gravity()

        self.draw_arrow()
