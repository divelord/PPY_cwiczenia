"""
ZAD07

Napisz generator, który zwraca słowa z pliku. Zgłoś wyjątek NoRingException,
jeśli generator zakończy działanie bez zwrócenia słowa "ring".
"""
from exceptions import NoRingException


def check_for_ring(path):
    found = False

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            word_lst = line.split()
            for word in word_lst:
                clean_word = word.strip(".,!?;:()\"'").lower()
                if clean_word == "ring":
                    found = True
                yield clean_word

    if not found:
        raise NoRingException()


try:
    for word in check_for_ring("../THE_HOBBIT.txt"):
        pass
except NoRingException as e:
    print(e)
