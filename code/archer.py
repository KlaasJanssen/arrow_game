import pygame
from arrow import Arrow
from math import atan2, degrees, radians, cos, sin

class Archer(pygame.sprite.Sprite):
    def __init__(self, pos, current_level, blood_particles):
        super().__init__()

        # Setup
        self.screen = pygame.display.get_surface()
        self.pos = pos
        self.current_level = current_level

        self.image = pygame.image.load('../assets/archer.png').convert_alpha()
        #self.image.fill((0,0,0))
        self.rect = self.image.get_rect(bottomleft = pos)

        # Arrows
        self.blood_particles = blood_particles
        self.arrows = pygame.sprite.Group()
        self.arrow_available = True
        self.max_countdown = 60
        self.arrow_countdown = 0

        # Bow
        self.direction = pygame.math.Vector2(0,0)
        self.angle = 0
        self.power = 0
        self.bow_drawn = False

        # Bow graphics
        self.original_bow_surf = pygame.image.load('../assets/bow.png').convert_alpha()
        self.arrow_surf = pygame.image.load('../assets/arrow.png').convert_alpha()
        #18, 50

    def get_input(self):
        self.get_direction()
        if pygame.mouse.get_pressed()[0]:
            if self.arrow_available:
                self.bow_drawn = True
                self.power += 0.2
                if self.power > 15: self.power = 15
        elif self.bow_drawn:
            if self.power >= 1:
                arrow_pos = self.get_arrow_pos()
                self.arrows.add(Arrow(arrow_pos, pygame.math.Vector2(self.direction * self.power), self.current_level, self.blood_particles))
                self.arrow_countdown = self.max_countdown
                self.arrow_available = False
            self.bow_drawn = False
            self.power = 0

    def update_countdown(self):
        self.arrow_countdown -= 1
        if self.arrow_countdown <= 0:
            self.arrow_available = True

    def get_direction(self):
        mouse_pos = pygame.mouse.get_pos()
        self.direction = pygame.math.Vector2(mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery).normalize()
        self.angle = degrees(atan2(self.direction[0], self.direction[1]))

    def show_arrow_path(self):
        if self.arrow_available:
            power = self.power
            if power < 2: power = 2
            pos = self.get_arrow_pos()
            velocity = power * self.direction
            radius = 10
            radiusminus = 1
            for i in range(101):
                pos += velocity
                velocity[1] += 0.1
                if i % 5 == 0 and not i == 0 and not i == 1:
                    pygame.draw.circle(self.screen, (255,255,255), pos, radius)
                    radiusminus += 1
                    if radiusminus % 2 == 1:
                        radius -= 1

    def get_arrow_pos(self):
        drawn_back = 20 * (self.power ** 2) / (18 + self.power ** 2)
        length = 40 - drawn_back

        x = sin(radians(self.angle)) * length
        y = cos(radians(self.angle)) * length

        pos = (self.pos[0] + 18 + x, self.pos[1] - 50 + y)
        return pos


    def draw_bow(self):
        bow_surf = self.original_bow_surf.copy()
        pygame.draw.line(bow_surf, (0,0,0), (90, 30), (119, 30), 5)
        if not self.arrow_available:
            pygame.draw.line(bow_surf, (255,255,255), (110,0), (110, 60))
        else:
            drawn_back = 20 * (self.power ** 2) / (18 + self.power ** 2)
            #pygame.draw.line(bow_surf, (0,0,0), (90, 30), (90 - drawn_back, 30), 5)

            self.arrow_rect = self.arrow_surf.get_rect(midleft = (110 - drawn_back, 30))
            bow_surf.blit(self.arrow_surf, self.arrow_rect)
            pygame.draw.lines(bow_surf, 'white', False, [(110,0), (110 - drawn_back, 30), (110, 60)])
            pygame.draw.rect(bow_surf, (0,0,0), pygame.Rect(90 - drawn_back, 28, drawn_back, 5), 0, 5)

        self.bow_surf = pygame.transform.rotozoom(bow_surf, self.angle - 90, 1)
        self.bow_rect = self.bow_surf.get_rect(center = (self.pos[0] + 18, self.pos[1] - 50))
        self.screen.blit(self.bow_surf, self.bow_rect)

    def update(self, enemies, obstacles):
        # Updates
        self.get_input()
        self.update_countdown()
        self.arrows.update(enemies, obstacles)

        # Draw
        self.draw_bow()
        self.arrows.draw(self.screen)
        self.show_arrow_path()
