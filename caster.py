from ray import Ray
import math
import settings
import pygame
from vector import Vector

class Caster:
    
    def __init__(self, rays_amt):
        self.rays = []
        self.position = Vector(0, 0)
        for i in range(rays_amt):
            ray = Ray(0, 0)
            ray.set_angle(math.radians(i))
            self.rays.append(ray)

    def set_angle(self, angle):
        for i, ray in enumerate(self.rays):
            ray.set_angle(math.radians(angle+i))
    
    def set_pos(self, x, y):
        self.position.x = x
        self.position.y = y
        for ray in self.rays:
            ray.position.x = x
            ray.position.y = y
    
    def draw(self, surface, bounds):
        for i, ray in enumerate(self.rays):
            nearest = None
            for b in bounds:
                points = []
                points.append(ray.cast(b.a, b.b))
                points.append(ray.cast(b.b, b.c))
                points.append(ray.cast(b.c, b.d))
                points.append(ray.cast(b.d, b.a))
                b.draw(surface)
                for point in points:
                    if point:
                        if nearest is None:
                            nearest = point
                        if ray.position.distance(point) < ray.position.distance(nearest):
                            nearest = point
            ray.draw(surface, point=nearest)
            if nearest:
                width = (settings.DISPLAY[0] / settings.RAYS) - 1
                dist = ray.position.distance(nearest)
                if dist == 0:
                    dist = 1


                color = (255, 255, 255)

                height = (settings.HEIGHT * settings.DISPLAY[1]) / dist
                if height > settings.DISPLAY[1]:
                    height = settings.DISPLAY[1]
                    
                offset = settings.DISPLAY[1]/2 - height / 2
                # pygame.draw.rect(surface, color, (i*width, offset, width, height))