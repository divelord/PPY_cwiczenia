"""
ZAD06

Znajdź najdłuższe słowo w pliku i wypisz je
"""

with open("../THE_HOBBIT.txt", "r", encoding="utf-8") as file:
    words = file.read().strip().split()

print(max(words, key=len))
