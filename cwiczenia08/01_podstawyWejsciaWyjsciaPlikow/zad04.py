"""
ZAD04

Znajdź, ile razy słowo "Bilbo" pojawia się w tekście
(z uwzględnieniem wielkości liter).
"""

with open("../THE_HOBBIT.txt", "r", encoding="utf-8") as file:
    words = file.read().strip().split()

word_to_find = "Bilbo"
print(words.count(word_to_find))
