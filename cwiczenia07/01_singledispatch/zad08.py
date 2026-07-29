"""
ZAD08

Zaimplementuj funkcję reverse(value):
• dla list → zwraca odwróconą listę,
• dla str → zwraca odwrócone słowa w napisie.
"""
from functools import singledispatch


@singledispatch
def reverse(value):
    return "Unknown type"


@reverse.register(list)
def _(value):
    return value[::-1]


@reverse.register(str)
def _(value):
    result = value.split()
    return " ".join([str(x)[::-1] for x in result])


print(reverse(["a", "b", "c"]))
print(reverse("abc"))
print(reverse("abc def"))
