import pygame

from Vec2 import Vec2

class cDynamicShape:
    def __init__(self, InitPos, InitWidth, InitHeight, InitVelocity, InitSpeed, InitColor, Screen, ScreenRect):
        self.Pos = InitPos
        self.Velocity = InitVelocity
        self.Speed = InitSpeed
        self.Width = InitWidth
        self.Height = InitHeight
        self.Color = InitColor
        self.Screen = Screen
        self.ScreenRect = ScreenRect

    def Select(self):
        pass

    def Deselect(self):
        pass

    def Update(self, fElapsedTime, MousePos):
        if self.Selected:
            if not self.CollidePoint(MousePos):
                self.Pos += ((self.Pos - MousePos).GetNormalized() * -1) * self.Speed * fElapsedTime

    def ClampToScreen(self):
        pass

    def CollidePoint(self, Point):
        pass

    def CheckCollision(self, other):
        pass

    def Draw(self):
        pass


class cCircle(cDynamicShape):
    def __init__(self, InitPos, InitRadius, InitVelocity, InitSpeed, InitColor, Screen, ScreenRect):
        self.Radius = InitRadius
        Diameter = self.Radius * 2
        cDynamicShape.__init__(self, InitPos - Vec2(self.Radius, self.Radius), Diameter, Diameter, InitVelocity, InitSpeed, InitColor, Screen, ScreenRect)
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

    def ClampToScreen(self):
        if self.Pos.x - self.Radius < self.ScreenRect.left:
            self.Pos.x = self.Radius

        if self.Pos.x + self.Radius > self.ScreenRect.right:
            self.Pos.x = self.ScreenRect.right - self.Radius

        if self.Pos.y - self.Radius < self.ScreenRect.top:
            self.Pos.y = self.Radius

        if self.Pos.y + self.Radius > self.ScreenRect.bottom:
            self.Pos.y = self.ScreenRect.bottom - self.Radius

    def CheckCollision(self, OtherCircle):
        return (self.Pos - OtherCircle.Pos).GetLengthSq() <= (OtherCircle.Radius + self.Radius) ** 2

    def CollidePoint(self, Point):
        return (self.Pos - Point).GetLengthSq() <= self.Radius ** 2

    def Draw(self):
        pygame.draw.circle(self.Screen, self.Color, (int(self.Pos.x), int(self.Pos.y)), self.Radius, self.Radius)

        """
        #Here's what the pygame.draw.circle function does; the only reason I don't use this code is because
        #it's slow as a result of the awful speed Python is known for, and pygame uses c++.

        for y in range(self.Radius * 2):
            y += self.Pos.y - self.Radius
            for x in range(self.Radius * 2):
                x += self.Pos.x - self.Radius

                if (self.Pos.x - x) ** 2 + (self.Pos.y - y) ** 2 <= self.Radius ** 2:
                    self.Screen.set_at((int(x), int(y)), self.Color)
        """


class cRectangle(cDynamicShape):
    def __init__(self, InitPos, InitWidth, InitHeight, InitVelocity, InitSpeed, InitColor, Screen, ScreenRect):
        cDynamicShape.__init__(self, InitPos, InitWidth, InitHeight, InitVelocity, InitSpeed, InitColor, Screen, ScreenRect)
        self.Rect = pygame.Rect(InitPos.x, InitPos.y, InitWidth, InitHeight)

    def Select(self):
        pass

    def Deselect(self):
        pass

    def ClampToScreen(self):
        pass

    def CheckCollision(self, other):
        pass

    def CollidePoint(self, Point):
        pass

    def Draw(self):
        pygame.draw.rect(self.Screen, self.Color, self.Rect)

