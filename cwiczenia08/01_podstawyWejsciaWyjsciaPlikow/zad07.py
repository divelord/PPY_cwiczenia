"""
ZAD07

Policz, ile unikalnych słów występuje w pliku.
"""

with open("../THE_HOBBIT.txt", "r", encoding="utf-8") as file:
    words = file.read().lower().strip().split()

print(len(set(words)))
