"""
ZAD01

Napisz dekorator argMap, który dodaje metodę mapOfArgs() do udekorowanej funkcji.
• Dekorator zakłada, że funkcja przyjmuje dokładnie jeden argument.
• Metoda mapOfArgs() powinna zwracać słownik:
    - klucze: argumenty przekazane do funkcji,
    - wartości: liczba użyć danego argumentu.
"""

import functools


def argMap(func):
    dct = {}

    @functools.wraps(func)
    def wrapper(arg):
        dct[arg] = dct.get(arg, 0) + 1
        return func(arg)

    def mapOfArgs():
        return dct

    wrapper.mapOfArgs = mapOfArgs

    return wrapper


@argMap
def greet(name):
    print(f"Hello {name}")


greet("A")
greet("B")
greet("C")
greet("D")
greet("A")
print(greet.mapOfArgs())
