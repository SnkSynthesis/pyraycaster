import pygame
from . import settings
from .boundary import Boundary
from .caster import Caster
import sys


pygame.init()
window = pygame.display.set_mode(settings.DISPLAY)
pygame.display.set_caption(settings.TITLE)
clock = pygame.time.Clock()


bounds = [
    Boundary(500, 310, 500, 500),
    Boundary(700, 500, 850, 500),
    Boundary(700, 300, 0, 500),
    Boundary(700, 301, 100, 100),
]

caster = Caster(360)

while True:
    clock.tick(settings.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(settings.BG_COLOR)

    x, y = pygame.mouse.get_pos()
    caster.set_pos(x, y)
    caster.draw(window, bounds)

    pygame.display.update()

pygame.quit()
