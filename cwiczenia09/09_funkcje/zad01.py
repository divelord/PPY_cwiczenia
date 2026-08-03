"""
ZAD01

Napisz funkcję, która przyjmuje dowolną liczbę argumentów pozycyjnych i zwraca ich sumę.
"""


def sum_elements(*args):
    return sum(args)


print(sum_elements(1, 2, 3, 4, 5, 6, 7, 8, 9))
