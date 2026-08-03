"""
ZAD02

Dany jest słownik, w którym wartościami są liczby.
Utwórz nowy słownik, w którym klucze i wartości są zamienione miejscami
(zakładamy, że wartości są unikalne).
"""


def swap_dct(dct):
    new_dct = {}

    for key, value in dct.items():
        new_dct[value] = key

    return new_dct


dct = {"a": 1, "b": 2, "c": 3, "d": 4}

print(swap_dct(dct))
