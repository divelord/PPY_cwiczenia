"""
ZAD04

Napisz funkcję, która zlicza, ile razy słowo "Bilbo" pojawia się w pliku.
Jeśli nie pojawia się ani razu, zgłoś własny wyjątek NoBilboException.
"""
from exceptions import NoBilboException


def check_for_bilbo(path):
    word_count = 0
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            word_lst = line.split()
            for word in word_lst:
                if word == "Bilbo":
                    word_count += 1

    if word_count == 0:
        raise NoBilboException()


try:
    check_for_bilbo("../THE_HOBBIT.txt")
except NoBilboException as e:
    print(e)
