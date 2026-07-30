"""
ZAD01

Napisz funkcję, która wczytuje plik hobbit.txt i zgłasza własny wyjątek FileEmptyException,
jeśli plik jest pusty.
"""
from exceptions import FileEmptyException


def check_file(path):
    with open(path, "r", encoding="utf-8") as file:
        if not file.read(1):
            raise FileEmptyException(path)


try:
    check_file("../THE_HOBBIT.txt")
except FileEmptyException as e:
    print(e)
