"""
ZAD01

Mając listę elementów o różnych typach, napisz funkcję, która zwraca słownik,
gdzie kluczami są typy elementów, a wartościami liczba ich wystąpień.
"""


def count_types(lst):
    dct = {}

    for i in lst:
        el = type(i).__name__

        if el not in dct:
            dct[el] = 0
        dct[el] += 1

    return dct


lst = [1, 2, "a", "b", "c", 2.5]

print(count_types(lst))
