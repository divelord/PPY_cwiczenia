"""
ZAD02

Napisz funkcję, która przyjmuje argumenty nazwane i zwraca listę wszystkich przekazanych wartości.
"""


def get_named_arguments(**kwargs):
    return list(kwargs.values())


print(get_named_arguments(name="abc", age=12))
