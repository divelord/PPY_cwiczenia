"""
ZAD01

Napisz funkcję, która wczytuje plik tekstowy i zwraca liczbę linii.
"""


def count_lines_from_file(path):
    line_count = 0

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line_count += 1

    return line_count


print(count_lines_from_file("example_text.txt"))
