import pygame, sys
from settings import screen_width, screen_height, vars
from level import Level
from button import Button, Level_Button
from game_data import levels
from level_select import Level_Select

class Game:
    def __init__(self):
        self.vars = vars
        self.vars.start_next_level = self.start_next_level
        self.vars.start_level = self.start_level
        self.vars.change_state_level_select = self.change_state_level_select
        self.level_select = Level_Select()
        #self.start_level()

    def start_level(self, level = None):
        if level == None:
            self.level = Level(self.vars.current_level)
        else:
            self.level = Level(level)
            self.vars.current_level = level

    def start_next_level(self):
        self.vars.current_level += 1
        if self.vars.current_level > len(levels):
            self.vars.current_level = len(levels)
        if self.vars.current_level > self.vars.max_level:
            self.vars.max_level = self.vars.current_level
        self.start_level()

    def run(self):
        if self.vars.state == 'active':
            self.level.run()
            if not self.level.state == 'active':
                self.level.level_end.draw()
        elif self.vars.state == 'level_select':
            self.level_select.run()

    def change_state_level_select(self):
        if self.level.state == 'won':
            if self.vars.max_level < self.level.current_level + 1:
                self.vars.max_level += 1
        self.vars.state = 'level_select'


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
