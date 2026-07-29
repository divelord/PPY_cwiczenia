"""
ZAD05

Zaimplementuj funkcję first(value):
• dla list → zwraca pierwszy element,
• dla str → zwraca pierwsze słowo.
"""
from functools import singledispatch


@singledispatch
def first(value):
    return "Unknown type"


@first.register(list)
def _(value):
    return value[0]


@first.register(str)
def _(value):
    result = value.split(" ")
    return result[0]


print(first(["a", "b", "c"]))
print(first("abc"))
print(first("abc def"))
