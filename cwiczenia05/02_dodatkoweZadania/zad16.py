"""
ZAD16

Utwórz klasę Vector2D z:
• x, y
• dodawaniem wektorów (__add__)
• reprezentacją tekstową
"""


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'({self.x}, {self.y})'


v1 = Vector2D(1, 2)
v2 = Vector2D(2, 3)
v3 = v1 + v2
print(v1)
print(v2)
print(v3)
