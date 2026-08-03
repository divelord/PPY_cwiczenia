"""
ZAD01

Mając listę liczb, utwórz nową listę, w której każdy element
jest sumą dwóch sąsiednich elementów z listy wejściowej.
"""


def sum_neighbouring_elements(lst):
    new_lst = []

    for i in range(1, len(lst) - 1):
        new_lst.append(lst[i - 1] + lst[i + 1])

    return new_lst


lst = [1, 2, 3, 4, 5]

print(sum_neighbouring_elements(lst))
