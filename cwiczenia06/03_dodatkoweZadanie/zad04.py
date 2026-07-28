"""
ZAD04

Napisz dekorator fabrykujący checktypes(*types).
• Sprawdza, czy pierwsze n argumentów pozycyjnych odpowiada zadanym typom.
• Jeśli przekazano zbyt mało argumentów:
    raise IndexError('Zbyt mało argumentów pozycyjnych.')
• Jeśli typy się nie zgadzają:
    raise TypeError('Niepoprawne typy argumentów.')
"""

import functools


def checktypes(*types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) < len(types):
                raise IndexError("Zbyt mało argumentów pozycyjnych")

            for i, j in zip(types, args):
                if not isinstance(j, i):
                    raise TypeError("Niepoprawne typy argumentów")

            return func(*args, **kwargs)

        return wrapper

    return decorator


@checktypes(int, int, int)
def test(a, b, c):
    return a + b + c


try:
    print(test(1, 2, 3))
    print(test(1, 2, 'a'))
    print(test(1, 2))
except IndexError as e:
    print(e)
except TypeError as e:
    print(e)
