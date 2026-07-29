"""
ZAD06

Zaimplementuj funkcję is_empty(value):
• dla list → zwraca informację, czy lista jest pusta,
• dla str → zwraca informację, czy napis jest pusty.
"""
from functools import singledispatch


@singledispatch
def is_empty(value):
    return "Unknown type"


@is_empty.register(list)
def _(value):
    if len(value) == 0:
        return "List is empty"
    return "List is not empty"


@is_empty.register(str)
def _(value):
    if value == "":
        return "String is empty"
    return "String is not empty"


print(is_empty([]))
print(is_empty([1]))
print(is_empty(""))
print(is_empty(" "))
print(is_empty("a"))
