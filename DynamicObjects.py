import pygame

from Vec2 import Vec2

class DynamicObject:
    def __init__(self, InitRect, InitVelocity, InitColor, Screen, ScreenRect):
        self.Rect = InitRect
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
            self.Rect.x -= self.Velocity.x * fElapsedTime

        if self.MovingRight:
            self.Rect.x += self.Velocity.x * fElapsedTime

        if self.MovingUp:
            self.Rect.y -= self.Velocity.y * fElapsedTime

        if self.MovingDown:
            self.Rect.y += self.Velocity.y * fElapsedTime

        if self.Rect.left < self.ScreenRect.left:
            self.Rect.left = self.ScreenRect.left

        if self.Rect.right > self.ScreenRect.right:
            self.Rect.right = self.ScreenRect.right

        if self.Rect.top < self.ScreenRect.top:
            self.Rect.top = self.ScreenRect.top

        if self.Rect.bottom < self.ScreenRect.bottom:
            self.Rect.bottom = self.ScreenRect.bottom

    def Draw(self):
        self.Screen.fill(self.Color, self.Rect)

