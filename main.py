import pygame
import settings
from boundary import Boundary
from player import Player

def load_map(path):
    bounds = []
    with open(path) as f:
        y = 0
        x = 0
        for line in f:
            y += settings.WIDTH - 1
            x = 0
            for char in line:
                if char == 'W':
                    bounds.append(Boundary(x, y))
                x += settings.WIDTH - 1
    return bounds

def main():

    window = pygame.display.set_mode(settings.REAL_DISPLAY)
    pygame.display.set_caption(settings.TITLE)
    clock = pygame.time.Clock()
    run = True

    bounds = load_map('map.txt')

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
