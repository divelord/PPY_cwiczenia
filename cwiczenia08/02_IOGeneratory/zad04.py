"""
ZAD04

Napisz generator, który zwraca tylko niepuste linie.
"""


def read_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()
            if clean_line:
                yield clean_line


gen = read_lines("../THE_HOBBIT.txt")

for line in range(100):
    print(next(gen))
