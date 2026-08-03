"""
ZAD04

Napisz funkcję, która dla danego słownika zwraca listę jego kluczy posortowanych
według odpowiadających im wartości malejąco.
"""


def sort_keys_by_value(dct):
    return sorted(dct, key=lambda x: dct[x], reverse=True)


dct = {"a": 1, "b": 10, "c": 3}

print(sort_keys_by_value(dct))
