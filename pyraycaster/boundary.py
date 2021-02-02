import pygame
from . import settings
from .vector import Vector


class Boundary:
    def __init__(self, x1, y1, x2, y2):
        self.a = Vector(x1, y1)
        self.b = Vector(x2, y2)

    def draw(self, surface):
        pygame.draw.line(
            surface, settings.BOUNDARY_COLOR, (self.a.x, self.a.y), (self.b.x, self.b.y)
        )
