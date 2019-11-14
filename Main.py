import sys
from time import time
from random import randint

import pygame

from DynamicObjects import Circle
from Vec2 import Vec2

class Game:
    def __init__(self):
        pygame.init()
        self.Screen = pygame.display.set_mode((1200, 600))
        self.ScreenRect = self.Screen.get_rect()
        pygame.display.set_caption("School")

        self.Backgrounds = (
            (0, 0, 0),
            (0, 255, 0),
            (0, 0, 255),
        )

        self.BackgroundIndex = 0

        self.Circles = []
        for x in range(10):
            self.Circles.append(Circle(Vec2(randint(0, self.ScreenRect.width), randint(0, self.ScreenRect.height)), randint(10, 50), Vec2(0, 0), 400, (255, 255, 255), self.Screen, self.ScreenRect))
            self.Circles[-1].ClampToScreen()

        self.SelectedCircle = None

        self.fStartingTime = time()
        while True:
            fOld = self.fStartingTime
            self.fStartingTime = time()
            self.fElapsedTime = self.fStartingTime - fOld

            self.MousePos = Vec2(pygame.mouse.get_pos())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.KeydownEvents(event)
                elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                    self.MouseEvents(event)

            Collided = False
            for circle in self.Circles:
                if circle is not self.SelectedCircle and self.SelectedCircle is not None:
                    if circle.CheckCircleCollision(self.SelectedCircle):
                        self.SelectedCircle.Color = self.SelectedCircle.CollisionColor
                        circle.Color = circle.CollisionColor
                        Collided = True
                    else:
                        circle.Color = circle.InitColor

            if self.SelectedCircle is not None:
                self.SelectedCircle.Update(self.fElapsedTime, self.MousePos)
                self.SelectedCircle.ClampToScreen()

                if Collided:
                    self.SelectedCircle.Color = self.SelectedCircle.CollisionColor
                else:
                    self.SelectedCircle.Color = self.SelectedCircle.SelectedColor

            self.Screen.fill(self.Backgrounds[self.BackgroundIndex])

            for circle in self.Circles:
                if circle is not self.SelectedCircle or self.SelectedCircle is None:
                    circle.Draw()

            if self.SelectedCircle is not None:
                self.SelectedCircle.Draw()

            pygame.display.flip()

    def KeydownEvents(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.key == pygame.K_1:
            self.BackgroundIndex += 1

            if self.BackgroundIndex >= len(self.Backgrounds):
                self.BackgroundIndex = 0

        if event.key == pygame.K_2:
            self.BackgroundIndex -= 1

            if self.BackgroundIndex < 0:
                self.BackgroundIndex = len(self.Backgrounds) - 1

    def MouseEvents(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for circle in self.Circles:
                if circle.CollidePoint(self.MousePos):
                    if self.SelectedCircle is not None:
                        self.SelectedCircle.Deselect()
                        if circle is self.SelectedCircle:
                            self.SelectedCircle.Deselect()
                            self.SelectedCircle = None
                        else:
                            self.SelectedCircle = circle
                            self.SelectedCircle.Select()
                    else:
                        self.SelectedCircle = circle
                        self.SelectedCircle.Select()

Game()
