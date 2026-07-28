"""
ZAD12

Utwórz klasę Rectangle z:
• atrybutami: width, height
• metodą: area()
• metodą: perimeter()
• reprezentacją __str__
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f'Rectangle({self.width}, {self.height})'


rectangle = Rectangle(100, 200)
print(rectangle)
print(rectangle.area())
print(rectangle.perimeter())
