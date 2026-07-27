"""
ZAD08

Stwórz generator RGB_generator(), który w nieskończoność zwraca losowe kolory RGB
w formacie (R, G, B) z wartościami 0-255.
• Dodaj filtr do generowania tylko jasnych kolorów (r + g + b > 400)
"""

import random


def RGB_generator():
    while True:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        yield r, g, b


def color_filter(gen):
    for r, g, b in gen:
        if r + g + b > 400:
            yield r, g, b


for i, color in zip(range(5), color_filter(RGB_generator())):
    print(color)
