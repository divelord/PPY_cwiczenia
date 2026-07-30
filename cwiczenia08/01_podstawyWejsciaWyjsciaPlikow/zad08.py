"""
ZAD08

Utwórz słownik, w którym kluczami są słowa, a wartościami ich liczności.
Wypisz 10 najczęściej występujących słów.
"""

with open("../THE_HOBBIT.txt", "r", encoding="utf-8") as file:
    words = file.read().lower().strip().split()

word_dct = {}

for word in words:
    if word not in word_dct:
        word_dct[word] = 0
    word_dct[word] += 1

word_dct_sorted = sorted(word_dct.items(), key=lambda item: item[1], reverse=True)

print(word_dct_sorted[:10])
