"""
ZAD03

Napisz dekorator fabrykujący deprecated(new_name).
• Przy wywołaniu funkcji powinien:
    - działać normalnie,
    - wypisać ostrzeżenie:
        "!!! <stara_nazwa> jest przestarzała, użyj <nowa_nazwa> zamiast !!!"
"""

import functools


def deprecated(new_name):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"!!! {func.__name__} jest przestarzała, użyj {new_name} zamiast !!!")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@deprecated("new_sum")
def old_sum(a, b):
    return a + b


print(old_sum(1, 2))
