from vector import Vector
from caster import Caster
import math
import settings
import pygame

class Player:

    def __init__(self):
        self.position = Vector(500, 500)
        self.angle = 0
        self.caster = Caster(settings.RAYS)
        self.caster.set_angle(self.angle)

    def set_angle(self, angle):
        self.caster.set_angle(angle)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.position += self.caster.rays[(len(self.caster.rays)-1)//2].direction*5
        if keys[pygame.K_DOWN]:
            self.position -= self.caster.rays[(len(self.caster.rays)-1)//2].direction*5
        if keys[pygame.K_RIGHT]:
            self.angle += 5
        if keys[pygame.K_LEFT]:
            self.angle -= 5
        
        self.set_angle(self.angle)
        self.caster.set_pos(self.position.x, self.position.y)