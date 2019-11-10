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

    def ClampToScreen(self):
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


class Circle(DynamicObject):
    def __init__(self, InitPos, InitRadius, InitVelocity, InitColor, Screen, ScreenRect):
        self.Radius = InitRadius
        Diameter = self.Radius * 2
        super().__init__(InitPos, Diameter, Diameter, InitVelocity, InitColor, Screen, ScreenRect)
    
    def GetCenter(self):
        return Vec2(self.Pos.x + self.Radius, self.Pos.y + self.Radius)

    def CheckCircleCollision(self, OtherCircle):
        CircleCenter = self.GetCenter()
        OtherCircleCenter = OtherCircle.GetCenter()

        DistanceX = (OtherCircleCenter.x - CircleCenter.x) ** 2
        DistanceY = (OtherCircleCenter.y - CircleCenter.y) ** 2

        if DistanceX + DistanceY < (self.Radius ** 2 + OtherCircle.Radius ** 2) * 2:
            return True
        else:
            return False

    def Draw(self):
        pygame.draw.circle(self.Screen, self.Color, (int(self.Pos.x + self.Radius), int(self.Pos.y + self.Radius)), self.Radius, self.Radius)
