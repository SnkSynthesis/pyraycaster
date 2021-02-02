import pygame
from . import settings
from .boundary import Boundary
from .player import Player
import sys


def load_map(path):
    bounds = []
    with open(path) as f:
        y = 0
        x = 0
        for line in f:
            y += settings.WIDTH - 1
            x = 0
            for char in line:
                if char == "W":
                    bounds.append(Boundary(x, y))
                x += settings.WIDTH - 1
    return bounds


pygame.init()

window = pygame.display.set_mode(settings.REAL_DISPLAY)
pygame.display.set_caption(settings.TITLE)
clock = pygame.time.Clock()

bounds = load_map("map.txt")

player = Player()

while True:
    clock.tick(settings.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player.update()

    window.fill(settings.BG_COLOR)
    player.draw(window, bounds)
    pygame.display.update()
