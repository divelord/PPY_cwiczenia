"""
ZAD03

Napisz dekorator klasowy Repeat, który przyjmuje parametr n.
• Po zastosowaniu do funkcji wykonuje ją n razy i zwraca ostatni wynik.
• Powinien działać dla dowolnej sygnatury funkcji.
"""

import functools


class Repeat:
    def __init__(self, n):
        self.n = n

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None

            for i in range(self.n):
                result = func(*args, **kwargs)

            return result

        return wrapper


@Repeat(5)
def greet(name):
    print(f"Hello {name}")
    return f"Welcome {name}"


print(greet("XYZ"))
