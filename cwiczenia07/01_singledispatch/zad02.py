"""
ZAD02

Rozszerz funkcję process(value) o dodatkową obsługę:
• str → zwraca wersję napisu zapisaną wielkimi literami.
"""
from functools import singledispatch


@singledispatch
def process(value):
    return f"Unsupported"


@process.register(int)
def _(value):
    return 2 * value


@process.register(str)
def _(value):
    return value.upper()


print(process(2.5))
print(process(4))
print(process("abc"))
