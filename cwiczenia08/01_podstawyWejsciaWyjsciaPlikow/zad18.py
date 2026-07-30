"""
ZAD18

Wygeneruj histogram częstości słów i zapisz go do pliku.
"""

with open("../THE_HOBBIT.txt", "r", encoding="utf-8") as file:
    words = file.read().lower().strip().split()

word_dct = {}

for word in words:
    if word not in word_dct:
        word_dct[word] = 0
    word_dct[word] += 1

word_dct_sorted = sorted(word_dct.items(), key=lambda item: item[1], reverse=True)[:50]
max_len = max(len(word) for word, count in word_dct_sorted) + 1

with open("../hobbit_histogram.txt", "w", encoding="utf-8") as file:
    for word, count in word_dct_sorted:
        bar = "#" * (count // 50)

        file.write(f"{word:{max_len}}|{bar} {count}\n")
