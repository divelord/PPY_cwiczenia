"""
ZAD02

Użyj generatora, aby wypisać tylko pierwsze 10 linii pliku.
"""


def read_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line


gen = read_lines("../THE_HOBBIT.txt")

for line in range(10):
    print(next(gen))
