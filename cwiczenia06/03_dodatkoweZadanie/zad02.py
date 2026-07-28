"""
ZAD02

Napisz dekorator withDebug.
• Jeśli funkcja została wywołana z argumentem nazwanym DEBUG, dekorator powinien:
    - wypisać nazwę funkcji,
    - wypisać argumenty,
    - wypisać wartość zwracaną,
    - opcjonalnie wypisać znacznik czasu.
• Argument DEBUG nie może być przekazany do oryginalnej funkcji.
• Jeśli DEBUG nie został podany, funkcja powinna działać normalnie.
"""

import functools
from datetime import datetime


def withDebug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        debug = kwargs.pop("DEBUG", False)

        execution_time = datetime.now()
        result = func(*args, **kwargs)

        if debug:
            print(f"Funkcja: {func.__name__}")
            print(f"Argumenty pozycyjne: {args}")
            print(f"Argumenty nazwane: {kwargs}")
            print(f"Zwrócony wynik: {result}")
            print(f"Godzina wykonania: {execution_time.strftime('%H:%M:%S')}")

        return result

    return wrapper


@withDebug
def add(a, b):
    return a + b


@withDebug
def greet(name=""):
    return f"Hello, {name}"


print(add(1, 2))
print(add(5, 12, DEBUG=True))
print(greet(name="XYZ", DEBUG=True))
