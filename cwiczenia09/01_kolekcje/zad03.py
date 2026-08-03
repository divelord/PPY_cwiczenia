"""
ZAD03

Mając listę napisów, napisz funkcję, która na podstawie tej listy utwórz słownik,
w którym kluczami są napisy, a wartościami liczba ich wystąpień w liście.
"""


def count_elements(lst):
    dct = {}

    for i in lst:
        if i not in dct:
            dct[i] = 0
        dct[i] += 1

    return dct


lst = ["abc", "def", "ghi", "jkl", "abc"]

print(count_elements(lst))
