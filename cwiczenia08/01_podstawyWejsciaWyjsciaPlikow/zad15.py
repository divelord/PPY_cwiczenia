"""
ZAD15

Utwórz nowy plik hobbit_summary.txt, który zawiera:
• łączną liczbę słów
• łączną liczbę linii
• 5 najczęściej występujących słów
"""

with open("../THE_HOBBIT.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

text = "".join(lines).lower()
words = text.split()

line_count = len(lines)

word_dct = {}

for word in words:
    if word not in word_dct:
        word_dct[word] = 0
    word_dct[word] += 1

word_dict_top5 = sorted(word_dct.items(), key=lambda item: item[1], reverse=True)[:5]

with open("../hobbit_summary.txt", "w", encoding="utf-8") as file:
    file.write(f"Łączna liczba słów: {len(words)}\n")
    file.write(f"Łączna liczba linii: {line_count}\n")
    file.write(f"5 najczęściej występujących słów:\n")

    for key, value in word_dict_top5:
        file.write(f" - {key}: {value}\n")
