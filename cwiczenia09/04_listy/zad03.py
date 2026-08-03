"""
ZAD03

Mając listę liczb, przesuń wszystkie elementy o jedno miejsce w prawo
(ostatni element przechodzi na początek).
"""


def shift_to_right(lst):
    last_el = lst[-1]

    for i in range(len(lst) - 1, 0, -1):
        lst[i] = lst[i - 1]

    lst[0] = last_el

    return lst


lst = [1, 2, 3]

print(shift_to_right(lst))
