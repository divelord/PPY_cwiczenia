"""
ZAD03

Zaimplementuj funkcję describe(value) tak, aby:
• dla int zwracała "Integer",
• dla str zwracała "String",
• dla wszystkich pozostałych typów zwracała "Unknown type".
"""
from functools import singledispatch


@singledispatch
def describe(value):
    return "Unknown type"


@describe.register(int)
def _(value):
    return "Integer"


@describe.register(str)
def _(value):
    return "String"


print(describe(2))
print(describe("abc"))
print(describe(2.5))
