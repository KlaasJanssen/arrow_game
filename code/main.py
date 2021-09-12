import pygame, sys
from settings import screen_width, screen_height, vars
from level import Level
from button import Button
from game_data import levels

class Game:
    def __init__(self):
        self.vars = vars
        self.vars.start_next_level = self.start_next_level
        self.start_level()
        #self.button = Button((200,100), (200,125), 'Hello there', 50)

    def start_level(self):
        self.level = Level(self.vars.current_level)

    def start_next_level(self):
        self.vars.current_level += 1
        if self.vars.current_level > len(levels):
            #self.vars.current_level = len(levels)
            self.vars.current_level = 1

        self.start_level()

    def run(self):
        if self.vars.state == 'active':
            self.level.run()
            if not self.level.state == 'active':
                self.level.level_end.draw()
            #if self.button.update():
            #    print('Hello there')
            #self.button.draw()


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
