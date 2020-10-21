from ray import Ray
import math
import settings
import pygame

class Caster:
    
    def __init__(self, rays_amt):
        self.rays = []
        for i in range(rays_amt):
            ray = Ray(0, 0)
            ray.set_angle(math.radians(i))
            self.rays.append(ray)

    def set_angle(self, angle):
        for i, ray in enumerate(self.rays):
            ray.set_angle(math.radians(angle+i))
    
    def set_pos(self, x, y):
        for ray in self.rays:
            ray.position.x = x
            ray.position.y = y
    
    def draw(self, surface, bounds):
        for i, ray in enumerate(self.rays):
            nearest = None
            for b in bounds:
                point = ray.cast(b)
                if nearest is None:
                    nearest = point
                if point:
                    if ray.position.distance(point) < ray.position.distance(nearest):
                        nearest = point
            if nearest:
                w = settings.DISPLAY[0] / settings.RAYS
                dist = ray.position.distance(nearest)
                if dist == 0:
                    dist = 1
                h = (settings.HEIGHT * settings.DISPLAY[1]) / dist
                if h > settings.DISPLAY[1]:
                    h = settings.DISPLAY[1]
                pygame.draw.rect(surface, (255, 255, 255), (i*w, settings.DISPLAY[1]/2, w, h))