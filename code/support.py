import pygame
from os import walk

def import_folder(path):
    surface_list = []
    for _,__,imgs in walk(path):
        for img in imgs:
            surf = pygame.image.load(path + '/' + img).convert_alpha()
            surface_list.append(surf)
    return surface_list
