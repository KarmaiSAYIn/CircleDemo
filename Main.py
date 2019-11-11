import sys
from time import time
from random import randint

import pygame

from DynamicObjects import DynamicObject, Circle
from Vec2 import Vec2

class Game:
    def __init__(self):
        pygame.init()
        self.Screen = pygame.display.set_mode((1200, 600))
        self.ScreenRect = self.Screen.get_rect()
        pygame.display.set_caption("School")

        self.Backgrounds = (
            (0, 0, 0),
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255),
        )

        self.BackgroundIndex = 0

        self.Circles = []
        for x in range(10):
            self.Circles.append(Circle(Vec2(randint(0, self.ScreenRect.width), randint(0, self.ScreenRect.height)), randint(10, 50), Vec2(400, 400), (255, 255, 255), self.Screen, self.ScreenRect))

        self.fStartingTime = time()
        while True:
            fOld = self.fStartingTime
            self.fStartingTime = time()
            self.fElapsedTime = self.fStartingTime - fOld

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    self.KeydownEvents(event)
                elif event.type == pygame.KEYUP:
                    self.KeyupEvents(event)

            for circle in self.Circles:
                circle.Update(self.fElapsedTime)
                circle.ClampToScreen()

            self.Screen.fill(self.Backgrounds[self.BackgroundIndex])
            [circle.Draw() for circle in self.Circles]
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
            pass

        if event.key == pygame.K_RIGHT:
            pass

        if event.key == pygame.K_UP:
            pass

        if event.key == pygame.K_DOWN:
            pass

    def KeyupEvents(self, event):
        if event.key == pygame.K_LEFT:
            pass

        if event.key == pygame.K_RIGHT:
            pass

        if event.key == pygame.K_UP:
            pass

        if event.key == pygame.K_DOWN:
            pass

Game()
