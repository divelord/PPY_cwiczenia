"""
ZAD01

Mając listę napisów, utwórz słownik, w którym kluczami są pierwsze litery tych napisów,
a wartościami listy napisów zaczynających się na daną literę.
"""


def get_first_letters(lst):
    dct = {}

    for el in lst:
        key = el[0]

        if key not in dct:
            dct[key] = []
        dct[key].append(el)

    return dct


lst = ["abc", "def", "acvfg", "badsf", "asdg", "dasdf"]

print(get_first_letters(lst))
