"""
ZAD07

Zaimplementuj funkcję to_string(value):
• dla int → konwertuje wartość na napis,
• dla list → konwertuje wszystkie elementy na napisy i łączy je przecinkami.
"""
from functools import singledispatch


@singledispatch
def to_string(value):
    return "Unknown type"


@to_string.register(int)
def _(value):
    return str(value)


@to_string.register(list)
def _(value):
    return ','.join([str(x) for x in value])


print(to_string(5))
print(to_string(["a", "c", "c"]))
print(to_string(["a", 6, "c"]))
