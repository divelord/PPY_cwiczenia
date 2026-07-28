"""
ZAD06

Napisz dekorator memorize, który buforuje (zapamiętuje) wyniki funkcji dla danych argumentów.
• Dekorator powinien działać dla dowolnej sygnatury funkcji (użyj *args oraz **kwargs).
• Powtórne wywołania z tymi samymi argumentami powinny zwracać zapisany wynik zamiast ponownego obliczania.
Udekoruj następującą funkcję:

import time

def slow_add(a, b):
    '''Simulates a slow addition by sleeping for 1 second.'''
    time.sleep(1)
    print(f"Computing {a}+{b}...")
    return a + b

Wskazówki:
• Użyj słownika do przechowywania wyników.
• Użyj krotki argumentów oraz posortowanych elementów kwargs jako klucza.
• Rozważ użycie functools.wraps, aby zachować metadane funkcji.
"""

import functools
import time


def memorize(func):
    dct = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key in dct:
            return dct[key]

        dct[key] = func(*args, **kwargs)

        return dct[key]

    return wrapper


@memorize
def slow_add(a, b):
    print(f"Computing {a} + {b}...")
    time.sleep(1)
    return a + b


print(slow_add(2, 3))
print(slow_add(2, 3))
print(slow_add(3, 4))
