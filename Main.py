import sys

import pygame

def Main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("School")

    Backgrounds = [
        (0, 0, 0),
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
    ]
    BackgroundIndex = 0
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    BackgroundIndex += 1

                if event.key == pygame.K_DOWN:
                    BackgroundIndex -= 1

                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        try:
            screen.fill(Backgrounds[BackgroundIndex])
        except IndexError:
            BackgroundIndex = 1
        pygame.display.flip()


Main()
