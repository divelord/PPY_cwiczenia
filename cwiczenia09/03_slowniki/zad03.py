"""
ZAD03

Mając słownik, w którym kluczami są napisy, a wartościami listy liczb,
utwórz słownik, gdzie wartościami będą sumy tych list.
"""


def sum_dict_values(dct):
    new_dct = {}

    for key, value in dct.items():
        new_dct[key] = sum(value)

    return new_dct


dct = {"a": [1], "b": [1, 2], "c": [1, 2, 3]}

print(sum_dict_values(dct))
