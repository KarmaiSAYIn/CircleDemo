import sys
from time import time

import pygame

from DynamicObjects import DynamicObject
from Vec2 import Vec2

class Game:
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

        self.BackgroundIndex = 0
        self.Rectangle = DynamicObject(Vec2(0, 0), 100, 100, Vec2(1, 1), (255, 255, 255), self.Screen, self.ScreenRect)

        self.fStartingTime = time()
        while True:
            fOld = self.fStartingTime
            self.fStartingTime = time()
            self.fElapsedTime = self.fStartingTime - fOld

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.KeydownEvents(event)
                elif event.type == pygame.KEYUP:
                    self.KeyupEvents(event)

            self.Rectangle.Update(self.fElapsedTime)

            self.Screen.fill(self.Backgrounds[self.BackgroundIndex])
            self.Rectangle.Draw()
            pygame.display.flip()

    def KeydownEvents(self, event):
        if event.key == pygame.K_1:
            self.BackgroundIndex += 1

            if self.BackgroundIndex >= len(self.Backgrounds):
                self.BackgroundIndex = 0

        if event.key == pygame.K_2:
            self.BackgroundIndex -= 1

            if self.BackgroundIndex < 0:
                self.BackgroundIndex = len(self.Backgrounds) - 1

        if event.key == pygame.K_LEFT:
            self.Rectangle.MovingLeft = True

        if event.key == pygame.K_RIGHT:
            self.Rectangle.MovingRight = True

        if event.key == pygame.K_UP:
            self.Rectangle.MovingUp = True

        if event.key == pygame.K_DOWN:
            self.Rectangle.MovingDown = True

    def KeyupEvents(self, event):
        if event.key == pygame.K_LEFT:
            self.Rectangle.MovingLeft = False

        if event.key == pygame.K_RIGHT:
            self.Rectangle.MovingRight = False

        if event.key == pygame.K_UP:
            self.Rectangle.MovingUp = False

        if event.key == pygame.K_DOWN:
            self.Rectangle.MovingDown = False

Game()
