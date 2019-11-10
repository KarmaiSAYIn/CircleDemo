import sys
from time import time

import pygame

from DynamicObjects import DynamicObject, Circle
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
        self.Circle0 = Circle(Vec2(400, 400), 50, Vec2(400, 400), (255, 255, 255), self.Screen, self.ScreenRect)
        self.Circle1 = Circle(Vec2(600, 400), 50, Vec2(400, 400), (255, 255, 255), self.Screen, self.ScreenRect)

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

            self.Circle0.Update(self.fElapsedTime)
            self.Circle0.ClampToScreen()

            if self.Circle0.CheckCircleCollision(self.Circle1):
                self.Circle0.Color = (255, 0, 0)
            else:
                self.Circle0.Color = (255, 255, 255)

            self.Screen.fill(self.Backgrounds[self.BackgroundIndex])
            self.Circle1.Draw()
            self.Circle0.Draw()
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
            self.Circle0.MovingLeft = True

        if event.key == pygame.K_RIGHT:
            self.Circle0.MovingRight = True

        if event.key == pygame.K_UP:
            self.Circle0.MovingUp = True

        if event.key == pygame.K_DOWN:
            self.Circle0.MovingDown = True

    def KeyupEvents(self, event):
        if event.key == pygame.K_LEFT:
            self.Circle0.MovingLeft = False

        if event.key == pygame.K_RIGHT:
            self.Circle0.MovingRight = False

        if event.key == pygame.K_UP:
            self.Circle0.MovingUp = False

        if event.key == pygame.K_DOWN:
            self.Circle0.MovingDown = False

game = Game()
