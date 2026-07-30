"""
ZAD01

Wczytaj plik hobbit.txt i wypisz całą jego zawartość na konsolę.
"""

with open("../THE_HOBBIT.txt", "r", encoding="utf-8") as file:
    print(file.read())
