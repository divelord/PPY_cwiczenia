"""
ZAD05

Napisz funkcję, która czyta plik linia po linii i zgłasza wyjątek LineTooLongException,
jeśli jakakolwiek linia przekracza 200 znaków.
"""
from exceptions import LineTooLongException


def check_for_len(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if len(line) > 200:
                raise LineTooLongException(line)


try:
    check_for_len("../THE_HOBBIT.txt")
except LineTooLongException as e:
    print(e)
