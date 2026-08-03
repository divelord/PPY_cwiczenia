"""
ZAD02

Napisz funkcję, która zwraca wszystkie linie z pliku zawierające określone słowo.
"""


def get_lines_with_word(path, word):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if word in line:
                yield line.strip()


for line in get_lines_with_word("example_text.txt", "dzień"):
    print(line)
