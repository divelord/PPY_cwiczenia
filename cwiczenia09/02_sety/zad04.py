"""
ZAD04

Dane są dwie listy napisów.
Utwórz zbiór napisów, które występują tylko w jednej z list (symetryczna różnica),
a następnie zwróć ich liczbę.
"""


def get_symmetric_difference_number(lst1, lst2):
    result = set(lst1).symmetric_difference(set(lst2))

    return len(result)


lst1 = [1, 2, 3]
lst2 = [3, 5, 6]

print(get_symmetric_difference_number(lst1, lst2))
