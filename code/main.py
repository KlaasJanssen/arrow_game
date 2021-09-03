import pygame, sys
from settings import screen_width, screen_height, vars
from level import Level

class Game:
    def __init__(self):
        self.current_level = 1
        self.vars = vars
        self.start_level()

    def start_level(self):
        self.level = Level(self.current_level)

    def run(self):
        if self.vars.state == 'active':
            self.level.run()

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((150,236,236))
    game.run()

    pygame.display.update()
    clock.tick(60)
