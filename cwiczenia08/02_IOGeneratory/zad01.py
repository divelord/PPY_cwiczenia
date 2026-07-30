"""
ZAD01

Napisz generator read_lines(file_path), który zwraca kolejne linie z pliku hobbit.txt, jedną po drugiej.
"""


def read_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line


for line in read_lines("../THE_HOBBIT.txt"):
    print(line)
