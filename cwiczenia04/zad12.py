"""
ZAD12

Napisz generator symulujący rzuty sześcienną kostką do gry.
Wymagania
• generator powinien zwracać liczby całkowite z zakresu od 1 do 6,
• generator powinien działać w nieskończoność,
• do generowania liczb użyj funkcji random.randint(1,6).
"""

import random


def dice():
    while True:
        yield random.randint(1, 6)


for i, roll in zip(range(5), dice()):
    print(roll)
