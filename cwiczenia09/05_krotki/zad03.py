"""
ZAD03

Mając krotkę zawierającą różne typy danych, utwórz nową krotkę
zawierającą tylko elementy typu int.
"""


def get_integers(tpl):
    lst = []

    for el in tpl:
        if isinstance(el, int):
            lst.append(el)

    return tuple(lst)


tpl = (1, 4, "asdf", "sdvf", 2)

print(get_integers(tpl))
