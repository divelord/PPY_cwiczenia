"""
ZAD02

Utwórz klasę Geometry ze statycznymi metodami:
• circleArea(radius)
• rectangleArea(width, height)
• triangleArea(base, height)
"""
import math


class Geometry:
    @staticmethod
    def circleArea(radius):
        return math.pi * pow(radius, 2)

    @staticmethod
    def rectangleArea(width, height):
        return width * height

    @staticmethod
    def triangleArea(base, height):
        return base * height / 2


print(Geometry.circleArea(3))
print(Geometry.rectangleArea(4, 5))
print(Geometry.triangleArea(4, 6))
