import pygame

from Vec2 import Vec2

class DynamicObject:
    def __init__(self, InitPos, InitWidth, InitHeight, InitVelocity, InitColor, Screen, ScreenRect):
        self.Pos = InitPos
        self.Width = InitWidth
        self.Height = InitHeight
        self.Velocity = InitVelocity
        self.Color = InitColor
        self.Screen = Screen
        self.ScreenRect = ScreenRect

        self.MovingLeft = False
        self.MovingRight = False
        self.MovingUp = False
        self.MovingDown = False

    def Update(self, fElapsedTime):
        if self.MovingLeft:
            self.Pos.x -= self.Velocity.x * fElapsedTime

        if self.MovingRight:
            self.Pos.x += self.Velocity.x * fElapsedTime

        if self.MovingUp:
            self.Pos.y -= self.Velocity.y * fElapsedTime

        if self.MovingDown:
            self.Pos.y += self.Velocity.y * fElapsedTime

        if self.Pos.x < self.ScreenRect.left:
            self.Pos.x = self.ScreenRect.left

        if self.Pos.x + self.Width > self.ScreenRect.right:
            self.Pos.x = self.ScreenRect.right - self.Width

        if self.Pos.y < self.ScreenRect.top:
            self.Pos.y = self.ScreenRect.top

        if self.Pos.y + self.Height > self.ScreenRect.bottom:
            self.Pos.y = self.ScreenRect.bottom - self.Height

    def Draw(self):
        self.Screen.fill(self.Color, pygame.Rect(int(self.Pos.x), int(self.Pos.y), self.Width, self.Height))

