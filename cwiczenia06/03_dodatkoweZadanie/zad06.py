"""
ZAD06

Napisz dekorator fabrykujący valueBounds(bounds).
• Działa na funkcjach jednoargumentowych.
• Po wykonaniu funkcji:
    - jeśli wynik nie jest typu liczbowego:
        raise TypeError('Niepoprawny typ zwracanej wartości')
    - jeśli wynik jest poza zakresem:
        raise ValueError('Wartość poza dozwolonym zakresem')
"""

import functools


def valueBounds(bounds):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(arg):
            result = func(arg)

            if not isinstance(result, int):
                raise TypeError("Niepoprawny typ zwracanej wartości")

            min_val, max_val = bounds

            if not min_val <= result <= max_val:
                raise ValueError("Wartość poza dozwolonym zakresem")

            return result

        return wrapper

    return decorator


@valueBounds((0, 10))
def square(x):
    return x ** 2


try:
    for i in range(5):
        print(square(i))
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
