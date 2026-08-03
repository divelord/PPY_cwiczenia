"""
ZAD01

Napisz dekorator, który wypisuje argumenty przekazane do funkcji przed jej wykonaniem.
"""


def print_arguments(func):
    def wrapper(*args, **kwargs):
        print((args, kwargs))

        return func(*args, **kwargs)

    return wrapper


@print_arguments
def add(a, b):
    return a + b


print(add(1, 2))
