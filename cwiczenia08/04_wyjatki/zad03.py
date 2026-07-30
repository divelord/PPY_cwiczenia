"""
ZAD03

Zmodyfikuj poprzednie zadanie tak, aby sprawdzanie słowa "ring" było niewrażliwe na wielkość liter.
"""
from exceptions import NoRingException


def check_for_ring(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if "ring" in line.lower():
                return
        raise NoRingException(path)


try:
    check_for_ring("../THE_HOBBIT.txt")
except NoRingException as e:
    print(e)
