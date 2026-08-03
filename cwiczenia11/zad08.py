"""
ZAD08

Utwórz klasę Vector2D zawierającą:
• atrybuty instancji x oraz y,
• statyczną metodę distance(v1, v2), obliczającą odległość pomiędzy dwoma wektorami,
• metodę klasową zero(), zwracającą wektor w punkcie (0,0).
"""
import math


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def distance(v1, v2):
        return math.sqrt((v1.x - v2.x) ** 2 + (v1.y - v2.y) ** 2)

    @classmethod
    def zero(cls):
        return cls(0, 0)


v1 = Vector2D.zero()
v2 = Vector2D(4, 5)

print(f"({v1.x}, {v1.y})")
print(f"({v2.x}, {v2.y})")

print(Vector2D.distance(v1, v2))
print(Vector2D.distance(Vector2D(3, 5), Vector2D.zero()))
