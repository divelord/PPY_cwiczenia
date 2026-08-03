"""
ZAD01

Mając dwie listy liczb, utwórz zbiór elementów, które występują w obu listach,
ale tylko raz (bez duplikatów). Następnie przekształć wynik na posortowaną listę.
"""


def get_common_elements(lst1, lst2):
    result = set(lst1).intersection(set(lst2))

    return sorted(list(result))


lst1 = [1, 2, 3, 4, 5, 5]
lst2 = [5, 1, 2, 6, 7, 8]

print(get_common_elements(lst1, lst2))
