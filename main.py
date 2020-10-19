import pygame
import settings
from boundary import Boundary
from ray import Ray
from vector import Vector
from caster import Caster

def main():

    window = pygame.display.set_mode(settings.DISPLAY)
    pygame.display.set_caption(settings.TITLE)
    clock = pygame.time.Clock()
    run = True

    bounds = [
        Boundary(500, 310, 500, 500),
        Boundary(700, 500, 850, 500),
        Boundary(700, 300, 0, 500),
        Boundary(700, 301, 100, 100)
    ]

    caster = Caster(360)

    while run:
        clock.tick(settings.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill(settings.BG_COLOR)

        x, y = pygame.mouse.get_pos()
        caster.set_pos(x, y)
        caster.draw(window, bounds)

        pygame.display.update()

if __name__ == '__main__':
    main()
    pygame.quit()