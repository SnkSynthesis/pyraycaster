import pygame
import settings
from boundary import Boundary
from player import Player

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

    player = Player()

    while run:
        clock.tick(settings.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        player.update()

        window.fill(settings.BG_COLOR)

        player.caster.draw(window, bounds)

        pygame.display.update()

if __name__ == '__main__':
    main()
    pygame.quit()