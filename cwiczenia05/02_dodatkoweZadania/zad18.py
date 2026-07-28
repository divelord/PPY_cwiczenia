"""
ZAD18

Utwórz klasę bazową Shape oraz klasy pochodne: Circle, Rectangle.
Każda powinna implementować metodę area().
"""

import math


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circle = Circle(100)
rectangle = Rectangle(100, 200)
print(circle.area())
print(rectangle.area())
