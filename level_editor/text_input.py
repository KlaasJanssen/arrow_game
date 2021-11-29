import pygame
from settings import screen_width, screen_height

class Text_Input:
    def __init__(self, pos, desc, num, constraint):
        self.screen = pygame.display.get_surface()

        self.pos = pos
        self.description = desc
        self.numerical = int(num)
        self.constraint = constraint

        self.selected = False
        self.input_got = False
        self.numbers = {x: pygame.key.key_code(x) for x in "0123456789"}

        self.image = pygame.Surface((60,30))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(topleft = pos)

        self.desc_font = pygame.font.Font(None, 35)
        self.description_surf = self.desc_font.render(self.description, True, (255,255,255))
        self.description_rect = self.description_surf.get_rect(bottomright = (self.rect.bottomleft + pygame.math.Vector2(-10, 0)))

        self.text_font = pygame.font.Font(None, 28)
        self.text_surf = self.text_font.render(str(self.numerical), True, (0,0,0))
        self.text_rect = self.text_surf.get_rect(bottomleft = (self.rect.bottomleft + pygame.math.Vector2(5, -5)))

        self.indicator_animation_index = 0
        self.indicator_animation_speed = 1/30
        self.indicator_surf = self.text_font.render('|', True, (0,0,0))

    def detect_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.selected = True
        elif pygame.Rect(screen_width - 300, screen_height / 2 + 50, 300, screen_height).collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.selected = False
        elif pygame.Rect(screen_width - 300, 0, 300, screen_height).collidepoint(mouse_pos):
            if not pygame.mouse.get_pressed()[0]:
                pass
            else:
                self.selected = False
        else:
            self.selected = False
        #     self.update_num()
        # else:
        #     self.update_num()

    def update_num(self):
        #self.numerical = self.num_temp
        self.text_surf = self.text_font.render(str(self.numerical), True, (0,0,0))

    def change_num(self):
        if self.selected:
            num = str(self.numerical)
            keys = pygame.key.get_pressed()
            if not self.input_got:
                if 1 in keys:
                    self.input_got = True
                    if keys[pygame.K_BACKSPACE]:
                        if len(num) > 0:
                            num = num[:-1]
                    for number, value in self.numbers.items():
                        if keys[value]:
                            num += number
            else:
                if not 1 in keys:
                    self.input_got = False
            if num == '':
                num = '0'
            num = int(num)
            if self.constraint == 'height':
                if num >= screen_height:
                    num = screen_height
            elif self.constraint == 'width':
                if num >= screen_width:
                    num = screen_width
            self.numerical = num




    def draw(self):
        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, (100,100,100), self.rect, 2)

        self.screen.blit(self.description_surf, self.description_rect)
        self.text_rect = self.text_surf.get_rect(bottomleft = (self.rect.bottomleft + pygame.math.Vector2(5, -5)))
        self.screen.blit(self.text_surf, self.text_rect)

        if self.selected:
            self.indicator_animation_index += self.indicator_animation_speed
            if int(self.indicator_animation_index) % 2 == 0:
                self.indicator_rect = self.indicator_surf.get_rect(bottomleft = self.text_rect.bottomright + pygame.math.Vector2(0,-1))
                self.screen.blit(self.indicator_surf, self.indicator_rect)

    def update(self, num):
        if not self.selected:
            self.numerical = num
        self.detect_click()
        self.change_num()
        self.update_num()
        return self.numerical
