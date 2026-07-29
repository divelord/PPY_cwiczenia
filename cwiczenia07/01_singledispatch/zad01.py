"""
ZAD01

Zaimplementuj funkcję process(value) z użyciem @singledispatch tak, aby:
• dla int zwracała wartość pomnożoną przez 2,
• dla wszystkich pozostałych typów zwracała "Unsupported".
"""
from functools import singledispatch


@singledispatch
def process(value):
    return f"Unsupported"


@process.register(int)
def _(value):
    return 2 * value


print(process(2.5))
print(process(4))
