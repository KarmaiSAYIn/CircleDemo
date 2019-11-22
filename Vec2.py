import math

class Vec2:
    def __init__(self, InitX, InitY=None):
        if InitY is None:
            assert(type(InitX) == tuple)
            self.x = InitX[0]
            self.y = InitX[1]
        else:
            self.x = InitX
            self.y = InitY

    def __add__(self, OtherVec):
        return Vec2(self.x + OtherVec.x, self.y + OtherVec.y)

    def __sub__(self, OtherVec):
        return Vec2(self.x - OtherVec.x, self.y - OtherVec.y)

    def __mul__(self, Multiplier):
        return Vec2(self.x * Multiplier, self.y * Multiplier)

    def GetTuple(self):
        return tuple((self.x, self.y))

    def GetLengthSq(self):
        return self.x ** 2 + self.y ** 2

    def GetLength(self):
        return math.sqrt(self.GetLengthSq())

    def GetNormalized(self):
        return self * (1 / self.GetLength())

    def Normalize(self):
        Normalized = self.GetNormalized()

        self.x = Normalized.x
        self.y = Normalized.y

    def MirrorX(self):
        self.x *= -1

    def MirrorY(self):
        self.y *= -1

