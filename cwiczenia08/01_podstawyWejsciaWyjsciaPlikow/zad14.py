"""
ZAD14

Usuń popularne angielskie słowa funkcyjne (np. the, and, is, in)
i wypisz 10 najczęściej występujących pozostałych słów.
"""

with open("../THE_HOBBIT.txt", "r", encoding="utf-8") as file:
    words = file.read().lower().strip().split()

excluded_words = ["the", "a", "an", "that", "to", "of", "in", "for", "and", "is", "are"]
word_dct = {}

for word in words:
    if word not in excluded_words:
        if word not in word_dct:
            word_dct[word] = 0
        word_dct[word] += 1

wordDictSorted = sorted(word_dct.items(), key=lambda item: item[1], reverse=True)

print(wordDictSorted[:10])
