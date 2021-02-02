import pygame
from . import settings
from .vector import Vector


class Boundary:
    def __init__(self, x, y):
        self.a = Vector(x, y)
        self.b = Vector(x + settings.WIDTH, y)
        self.c = Vector(x + settings.WIDTH, y + settings.WIDTH)
        self.d = Vector(x, y + settings.WIDTH)

    def poly_points(self):
        return [tuple(self.a), tuple(self.b), tuple(self.c), tuple(self.d)]

    def draw(self, surface):
        pygame.draw.polygon(surface, settings.BOUNDARY_COLOR, self.poly_points(), 1)
