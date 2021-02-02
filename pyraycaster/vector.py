import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return len(Vector(self.x - other.x, self.y - other.y))

    def __len__(self):
        return int(math.sqrt(self.x ** 2 + self.y ** 2))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)

    def normalize(self):
        if len(self) != 0:
            self /= len(self)
