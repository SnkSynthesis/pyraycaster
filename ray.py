import pygame
import settings
from vector import Vector
import math


class Ray:
    def __init__(self, x, y):
        self.position = Vector(x, y)
        self.direction = Vector(1, 0)

    def look_at(self, x, y):
        self.direction.x = x - self.position.x
        self.direction.y = y - self.position.y
        self.direction.normalize()

    def set_angle(self, angle):
        self.direction.x = math.cos(angle)
        self.direction.y = math.sin(angle)

    def cast(self, boundary):

        x1 = boundary.a.x
        y1 = boundary.a.y
        x2 = boundary.b.x
        y2 = boundary.b.y

        x3 = self.position.x
        y3 = self.position.y
        x4 = self.position.x + self.direction.x
        y4 = self.position.y + self.direction.y

        denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denom == 0:
            return None

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denom

        if t > 0 and t < 1 and u > 0:
            point = Vector(x1 + t * (x2 - x1), y1 + t * (y2 - y1))
            return point
        else:
            return None

    def draw(self, surface, point=None):
        if point:
            pygame.draw.line(
                surface,
                settings.RAY_COLOR,
                (self.position.x, self.position.y),
                (point.x, point.y),
            )
        else:
            screen_vec = Vector(settings.DISPLAY[0], settings.DISPLAY[1])
            pygame.draw.line(
                surface,
                settings.RAY_COLOR,
                (self.position.x, self.position.y),
                (
                    self.position.x + self.direction.x * len(screen_vec),
                    self.position.y + self.direction.y * len(screen_vec),
                ),
            )
