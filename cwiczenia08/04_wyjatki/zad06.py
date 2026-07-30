"""
ZAD06

Utwórz funkcję, która wyszukuje frazę "my precious" i zgłasza wyjątek NoPreciousException,
jeśli nie zostanie ona znaleziona.
"""
from exceptions import NoPreciousException


def check_for_precious(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if "my precious" in line.lower():
                return
        raise NoPreciousException(path)


try:
    check_for_precious("../THE_HOBBIT.txt")
except NoPreciousException as e:
    print(e)
