import sys
from time import time
from random import randint

import pygame

from DynamicObjects import cCircle, cRectangle
from Vec2 import Vec2

class Game:
    def __init__(self):
        pygame.init()
        self.Screen = pygame.display.set_mode((1200, 600))
        self.ScreenRect = self.Screen.get_rect()
        pygame.display.set_caption("School")

        self.Font = pygame.sysfont.SysFont(None, 48)

        self.Backgrounds = (
            (0, 0, 0),
            (0, 255, 0),
            (0, 0, 255),
        )

        self.BackgroundIndex = 0

        # This will be hard-coded until the map creator is made:
        self.Points = ((77, 552), (131, 170), (386, 270), (487, 83), (640, 321), (742, 529), (478, 481), (1108, 28), (1100, 251), (971, 412))

        self.Shapes = []
        for x in range(10):
            self.Shapes.append(cCircle(Vec2(self.Points[x]), randint(10, 50), Vec2(0, 0), 400, (255, 255, 255), self.Screen, self.ScreenRect))
            self.Shapes[-1].ClampToScreen()

        self.SelectedShape = None

        self.fStartingTime = time()

        nFrameCounter = 0
        self.FPS = 0
        while True:
            fOld = self.fStartingTime
            self.fStartingTime = time()
            self.fElapsedTime = self.fStartingTime - fOld
            nFrameCounter += 1

            if nFrameCounter % 10 == 0:
                try:
                    self.FPS = round(1 / self.fElapsedTime)
                except ZeroDivisionError:
                    self.FPS = self.FPS

            self.MousePos = Vec2(pygame.mouse.get_pos())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.KeydownEvents(event)
                elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                    self.MouseEvents(event)

            Collided = False
            for shape in self.Shapes:
                if shape is not self.SelectedShape and self.SelectedShape is not None:
                    if shape.CheckCollision(self.SelectedShape):

                        self.SelectedShape.Color = self.SelectedShape.CollisionColor
                        shape.Color = shape.CollisionColor
                        Collided = True
                    else:
                        shape.Color = shape.InitColor

            if self.SelectedShape is not None:
                self.SelectedShape.Update(self.fElapsedTime, self.MousePos)
                self.SelectedShape.ClampToScreen()

                if Collided:
                    self.SelectedShape.Color = self.SelectedShape.CollisionColor
                else:
                    self.SelectedShape.Color = self.SelectedShape.SelectedColor

            self.Screen.fill(self.Backgrounds[self.BackgroundIndex])

            for shape in self.Shapes:
                if shape is not self.SelectedShape or self.SelectedShape is None:
                    shape.Draw()

            if self.SelectedShape is not None:
                self.SelectedShape.Draw()

            self.Screen.blit(pygame.font.Font.render(self.Font, str(self.FPS), True, (255, 255, 255)), (0, 0))
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

            CursorCollisionHappend = False
            for shape in self.Shapes:
                if shape.CollidePoint(self.MousePos):
                    CursorCollisionHappend = True
                    if self.SelectedShape is not None:
                        self.SelectedShape.Deselect()

                        if shape is self.SelectedShape:
                            self.SelectedShape = None
                        elif not CursorCollisionHappend:
                            self.SelectedShape = shape
                            self.SelectedShape.Select()
                    else:
                        self.SelectedShape = shape
                        self.SelectedShape.Select()

Game()
