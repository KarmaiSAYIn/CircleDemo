import pygame

from Vec2 import Vec2

class DynamicObject:
    def __init__(self, InitPos, InitWidth, InitHeight, InitVelocity, InitSpeed, InitColor, Screen, ScreenRect):
        self.Pos = InitPos
        self.Velocity = InitVelocity
        self.Speed = InitSpeed
        self.Width = InitWidth
        self.Height = InitHeight
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
    def __init__(self, InitPos, InitRadius, InitVelocity, InitSpeed, InitColor, Screen, ScreenRect):
        self.Radius = InitRadius
        Diameter = self.Radius * 2
        DynamicObject.__init__(self, InitPos, Diameter, Diameter, InitVelocity, InitSpeed, InitColor, Screen, ScreenRect)
        self.InitColor = InitColor
        self.SelectedColor = (255, 0, 0)
        self.CollisionColor = (0, 200, 150)

        self.Selected = False

    def Select(self):
        self.Selected = True

        self.Color = self.SelectedColor

    def Deselect(self):
        self.Selected = False

        self.Color = self.InitColor

    def Update(self, fElapsedTime, MousePos):
        if self.Selected:
            if not self.CollidePoint(MousePos):
                self.Pos += (((self.Pos + Vec2(self.Radius, self.Radius)) - MousePos).GetNormalized() * -1) * self.Speed * fElapsedTime

    def GetCenter(self):
        return Vec2(self.Pos.x + self.Radius, self.Pos.y + self.Radius)

    def CheckCircleCollision(self, OtherCircle):
        CircleCenter = self.GetCenter()
        OtherCircleCenter = OtherCircle.GetCenter()

        DistanceX = (OtherCircleCenter.x - CircleCenter.x) ** 2
        DistanceY = (OtherCircleCenter.y - CircleCenter.y) ** 2

        return DistanceX + DistanceY <= (OtherCircle.Radius + self.Radius) ** 2

    def CollidePoint(self, Point):
        return (self.GetCenter() - Point).GetLengthSq() <= self.Radius ** 2

    def Draw(self):
        pygame.draw.circle(self.Screen, self.Color, (int(self.Pos.x + self.Radius), int(self.Pos.y + self.Radius)), self.Radius, self.Radius)

        """
        #Here's what the pygame.draw.circle function does; the only reason I don't use this code is because
        #it's slow as a result of the awful speed Python is known for, and pygame uses c++.

        for y in range(self.Radius * 2):
            y += self.Pos.y - self.Radius
            for x in range(self.Radius * 2):
                x += self.Pos.x - self.Radius

                if (self.Pos.x - x) ** 2 + (self.Pos.y - y) ** 2 <= self.Radius ** 2:
                    self.Screen.set_at((x, y), self.Color)
                    """

