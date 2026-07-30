"""
ZAD10

Oblicz średnią długość słowa w tekście.
"""

with open("../THE_HOBBIT.txt", "r", encoding="utf-8") as file:
    words = file.read().strip().split()

print(sum(len(word) for word in words) / len(words))
