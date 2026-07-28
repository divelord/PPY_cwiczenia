"""
ZAD23

Zaimplementuj funkcję:
def compose(*funcs):
    ...
gdzie funcs to krotka funkcji.
Funkcja powinna zwrócić nową funkcję będącą złożeniem podanych funkcji (od prawej do lewej).
"""


def compose(*funcs):
    def composed(x):
        result = x

        for func in reversed(funcs):
            result = func(result)

        return result

    return composed


def add(x):
    return x + 5


def multiply(x):
    return x * 2


def square(x):
    return x ** 2


print(compose(add, multiply, square)(2))
