"""
ZAD02

Utwórz własny wyjątek NoRingException i napisz funkcję, która zgłasza go,
jeśli słowo "ring" nie występuje w pliku.
"""
from exceptions import NoRingException


def check_for_ring(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if "ring" in line:
                return
        raise NoRingException(path)


try:
    check_for_ring("../THE_HOBBIT.txt")
except NoRingException as e:
    print(e)
