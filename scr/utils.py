import os
import sys
import pygame


def get_path(*path):
    if getattr(sys, 'frozen', False):
        base_dir = getattr(sys, '_MEIPASS', os.path.dirname(sys.executable))
    else:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, *path)



def load_image(*path, size):
    image = pygame.image.load(get_path(*path))
    image = pygame.transform.scale(image, size)
    image.set_colorkey((0,0,0 ))
    return image
