"""
ZAD02

Napisz dekorator jako klasę o nazwie Timer.
• Klasa powinna implementować metodę __call__.
• Po zastosowaniu do funkcji powinna mierzyć czas jej wykonania i wypisywać go w sekundach.
• Dekorator powinien działać dla dowolnej sygnatury funkcji.
"""

import functools
import time


class Timer:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()

        print(f"czas wykonania: {end - start}")

        return result


@Timer
def add(a, b):
    return a + b


print(add(1, 2))
