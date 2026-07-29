"""
ZAD05

Inteligentny formatter
Utwórz klasę Formatter z metodą format(value):
• int → formatuj jako zapis binarny,
• float → formatuj z dokładnością do 2 miejsc po przecinku,
• list → formatuj każdy element rekurencyjnie.

Dodatkowo:
• Zaimplementuj __call__(), aby można było wywoływać obiekt jak funkcję,
• Zaimplementuj metodę __str__().
"""
from functools import singledispatchmethod


class Formatter:
    def __init__(self):
        self.result = ""

    @singledispatchmethod
    def format(self, value):
        result = str(value)
        self.result = result

        return result

    @format.register(int)
    def _(self, value):
        result = bin(value)
        self.result = result

        return result

    @format.register(float)
    def _(self, value):
        result = f"{round(value, 2)}"
        self.result = result

        return result

    @format.register(list)
    def _(self, value):
        el = [self.format(i) for i in value]
        result = ", ".join(el)
        self.result = result

        return result

    def __call__(self, value):
        return self.format(value)

    def __str__(self):
        return self.result


formatter = Formatter()

print(formatter(10))
print(formatter(1.5234))
print(formatter([1, 2, 4, 2.5345, [12, 5.3245]]))
