"""
ZAD01

Zdefiniuj funkcję przy użyciu singledispatch, która dla:
• liczby zwraca jej kwadrat,
• napisu zwraca jego długość
• listy zwraca jej pierwszy element
"""
from functools import singledispatch


@singledispatch
def fun(value):
    return "Unsupported type"


@fun.register(int)
def _(value):
    return value ** 2


@fun.register(str)
def _(value):
    return len(value)


@fun.register(list)
def _(value):
    return value[0]


print(fun(10))
print(fun("abc"))
print(fun(["a", "b", "c"]))
print(fun(2.5))
