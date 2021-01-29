import pygame
import settings
from boundary import Boundary
from player import Player


def main():

    window = pygame.display.set_mode(settings.REAL_DISPLAY)
    pygame.display.set_caption(settings.TITLE)
    clock = pygame.time.Clock()
    run = True

    bounds = [
        Boundary(500, 140),
        Boundary(400, 300),
        Boundary(310, 300 + settings.WIDTH),
        Boundary(320, 330 + settings.WIDTH * 2),
        Boundary(320, 300 + settings.WIDTH * 3),
        Boundary(300, 130),
        Boundary(341, 630),
        Boundary(749, 135),
        Boundary(234, 347),
    ]

    player = Player()

    while run:
        clock.tick(settings.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        player.update()

        window.fill(settings.BG_COLOR)

        player.draw(window, bounds)

        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
