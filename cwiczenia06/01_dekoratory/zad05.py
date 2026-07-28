"""
ZAD05

Napisz dekorator call_counter, który zlicza, ile razy dana funkcja została wywołana.
"""

import functools


def call_counter(func):
    count = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        wrapper.count = count

        return func(*args, **kwargs)

    wrapper.count = count

    return wrapper


@call_counter
def test():
    return "test"


test()
test()
test()

print(f"Liczba wywołań: {test.count}")
