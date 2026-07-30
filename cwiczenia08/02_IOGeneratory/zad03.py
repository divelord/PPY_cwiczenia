"""
ZAD03

Zmodyfikuj generator tak, aby usuwał białe znaki oraz znaki nowej linii z każdej linii.
"""


def read_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()


gen = read_lines("../THE_HOBBIT.txt")

for line in range(10):
    print(next(gen))
