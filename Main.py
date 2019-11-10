import sys
from time import time

import pygame

from DynamicObjects import DynamicObject
from Vec2 import Vec2

class Game:
    @staticmethod #This is probably redundant; but I'm trying to avoid making an instance of Game.
    def __init__(self):
        pygame.init()
        self.Screen = pygame.display.set_mode((1200, 800))
        self.ScreenRect = self.Screen.get_rect()
        pygame.display.set_caption("School")

        self.Backgrounds = (
            (0, 0, 0),
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255),
        )

        self.BackgroundIndex = 0;
        self.Rectangle = DynamicObject(pygame.Rect(0, 0, 100, 100), Vec2(200, 200), (255, 255, 255), self.Screen, self.ScreenRect)

        self.fElapsedTime = time()
        while True:
            self.fElapsedTime = time() - self.fElapsedTime

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.BackgroundIndex += 1

                        if self.BackgroundIndex >= len(self.Backgrounds):
                            self.BackgroundIndex = 0

                    if event.key == pygame.K_2:
                        self.BackgroundIndex -= 1

                        if self.BackgroundIndex < 0:
                            self.BackgroundIndex = len(self.Backgrounds) - 1

            self.Rectangle.Update(self.fElapsedTime)

            self.Screen.fill(self.Backgrounds[self.BackgroundIndex])
            self.Rectangle.Draw()
            pygame.display.flip()

Game(Game)
