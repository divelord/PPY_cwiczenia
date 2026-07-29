"""
ZAD04

Zaimplementuj funkcję length(value) z użyciem @singledispatch:
• dla list → zwraca liczbę elementów,
• dla str → zwraca długość napisu.
"""
from functools import singledispatch


@singledispatch
def length(value):
    return "Unknown type"


@length.register(list)
def _(value):
    return len(value)


@length.register(str)
def _(value):
    return len(value)


print(length([1, 2, 3]))
print(length("abc"))
print(length(3))
