from .vector import Vector
from .caster import Caster
from . import settings
import pygame


class Player:
    def __init__(self):
        self.position = Vector(600, 600)
        self.angle = 1000
        self.caster = Caster(settings.RAYS)
        self.caster.set_angle(self.angle)

    def set_angle(self, angle):
        self.caster.set_angle(angle)

    def draw(self, surface, bounds):
        self.caster.draw(surface, bounds)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.position += (
                self.caster.rays[(len(self.caster.rays) - 1) // 2].direction * 5
            )
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.position -= (
                self.caster.rays[(len(self.caster.rays) - 1) // 2].direction * 5
            )
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.angle += 5
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.angle -= 5

        self.set_angle(self.angle)
        self.caster.set_pos(self.position.x, self.position.y)