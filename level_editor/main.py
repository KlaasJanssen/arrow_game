import pygame
import sys
from settings import screen_width, screen_height, vars
from button import Button
from ground import Ground
from player import Player
from enemies import Enemies
from obstacles import Obstacles
from deleter import Deleter

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

class Editor:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.display_background = pygame.Surface((300, screen_height))
        self.display_background.fill((30,30,30))

        self.vars = vars

        self.buttons = []
        self.buttons.append(Button((screen_width - 275, 25), 'player'))
        self.buttons.append(Button((screen_width - 125, 25), 'enemy'))
        self.buttons.append(Button((screen_width - 275, 175), 'wood'))
        self.buttons.append(Button((screen_width - 125, 175), 'metal'))
        self.buttons.append(Button((screen_width - 275, 325), 'ground'))
        self.buttons.append(Button((screen_width - 125, 325), 'delete'))

        self.ground = Ground()
        self.player = Player()
        self.enemies = Enemies()
        self.obstacles = Obstacles()
        self.deleter = Deleter()

    def update_buttons(self):
        for button in self.buttons:
            button.update()
            button.draw()

    def display_control_background(self):
        self.screen.blit(self.display_background, (screen_width - 300,0))

    def run(self):
        self.display_control_background()
        self.update_buttons()
        self.ground.update()
        self.player.update(self.obstacles)
        self.enemies.update(self.obstacles)
        self.obstacles.update()
        self.deleter.update(self.player, self.enemies, self.obstacles)

        self.ground.draw()
        self.player.draw()
        self.enemies.draw()
        self.obstacles.draw()


editor = Editor()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((150,236,236))
    pygame.draw.line(screen, 'white', (screen_width - 300,0), (screen_width - 300, screen_height))
    editor.run()

    pygame.display.update()
    clock.tick(60)
