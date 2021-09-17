import pygame
from settings import vars

class Button:
    def __init__(self, pos, width, height, text, fontsize = 30, func = None, args = []):
        self.screen = pygame.display.get_surface()
        self.pos = pos
        self.width = int(width)
        self.height = int(height)
        self.text = text
        self.func = func
        self.args = args

        self.unpressed_surf = pygame.image.load('../assets/button_unpressed.png').convert_alpha()
        self.unpressed_surf = pygame.transform.scale(self.unpressed_surf, (self.width, self.height))
        self.pressed_surf = pygame.image.load('../assets/button_pressed.png').convert_alpha()
        self.pressed_surf = pygame.transform.scale(self.pressed_surf, (self.width, self.height))
        self.image = self.unpressed_surf
        self.rect = self.image.get_rect(center = self.pos)

        self.mouse_over_button = False
        self.clicked = False

        self.button_font = pygame.font.Font(None, fontsize)
        self.button_text_surf = self.button_font.render(self.text, True, 'white')
        self.button_text_rect = self.button_text_surf.get_rect(center = pos)



    def draw(self):
        if self.mouse_over_button:
            self.image = self.pressed_surf
        else:
            self.image = self.unpressed_surf

        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.button_text_surf, self.button_text_rect)

    def detect_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over_button = True
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            else:
                if self.clicked:
                    self.clicked = False
                    if not self.func == None:
                        self.func(*self.args)
                    else:
                        return True
        else:
            self.mouse_over_button = False
            self.clicked = False
        return False

    def update(self):
        return self.detect_click()

class Level_Button(Button):
    def __init__(self, pos, level, fontsize = 50):
        super().__init__(pos, 100, 100, str(level), fontsize)
        self.unpressed_surf = pygame.image.load('../assets/level_select_button_unpressed.png').convert_alpha()
        self.pressed_surf = pygame.image.load('../assets/level_select_button_pressed.png').convert_alpha()

        self.level = level
        self.vars = vars

        self.locked_surf = pygame.image.load('../assets/level_select_locked.png').convert_alpha()
        self.locked_rect = self.locked_surf.get_rect(center = pos)
        #self.locked_surf.fill((0,0,0,100))

    def detect_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over_button = True
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            else:
                if self.clicked:
                    self.clicked = False
                    if self.level <= self.vars.max_level:
                        self.vars.start_level(self.level)
                        self.vars.state = 'active'
        else:
            self.mouse_over_button = False
            self.clicked = False
        return False

    def draw(self):
        self.locked = not self.level <= self.vars.max_level
        if self.locked:
            self.image = self.unpressed_surf
        else:
            if self.mouse_over_button:
                self.image = self.pressed_surf
            else:
                self.image = self.unpressed_surf

        self.screen.blit(self.image, self.rect)
        if self.locked:
            self.screen.blit(self.locked_surf, self.locked_rect)
        self.screen.blit(self.button_text_surf, self.button_text_rect)
