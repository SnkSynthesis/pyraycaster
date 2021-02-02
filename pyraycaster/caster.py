from .ray import Ray
import math


class Caster:
    def __init__(self, rays_amt):
        self.rays = []
        for i in range(rays_amt):
            ray = Ray(0, 0)
            ray.set_angle(math.radians(i))
            self.rays.append(ray)

    def set_pos(self, x, y):
        for ray in self.rays:
            ray.position.x = x
            ray.position.y = y

    def draw(self, surface, bounds):
        for ray in self.rays:
            nearest = None
            for b in bounds:
                b.draw(surface)
                point = ray.cast(b)
                if nearest is None:
                    nearest = point
                if point:
                    if ray.position.distance(point) < ray.position.distance(nearest):
                        nearest = point
            ray.draw(surface, point=nearest)
