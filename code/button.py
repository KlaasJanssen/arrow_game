import pygame

class Button:
    def __init__(self, pos, width, height, text, fontsize = 30, func = None):
        self.screen = pygame.display.get_surface()
        self.pos = pos
        self.width = width
        self.height = height
        self.text = text
        self.func = func

        self.unpressed_surf = pygame.Surface((self.width, self.height))
        self.unpressed_surf.fill('red')
        self.pressed_surf = pygame.Surface((self.width, self.height))
        self.pressed_surf.fill('blue')
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
                        self.func()
                    else:
                        return True

        else:
            self.mouse_over_button = False
            self.clicked = False
        return False

    def update(self):
        return self.detect_click()
