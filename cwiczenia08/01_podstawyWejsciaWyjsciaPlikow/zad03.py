"""
ZAD03

Policz, ile słów znajduje się w pliku.
Traktuj słowa jako ciągi znaków rozdzielone białymi znakami.
"""

with open("../THE_HOBBIT.txt", "r", encoding="utf-8") as file:
    words = file.read().strip().split()

print(len(words))
