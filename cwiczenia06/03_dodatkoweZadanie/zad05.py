"""
ZAD05

Napisz dwa dekoratory:
• checkargs(*rules) – sprawdza zakresy wartości argumentów,
• minmaxarg – śledzi minimalną i maksymalną wartość argumentów numerycznych.
"""

import functools


def checkargs(*rules):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for val, (min_val, max_val) in zip(args, rules):
                if not min_val <= val <= max_val:
                    raise ValueError("Wartość poza zakresem")

            return func(*args, **kwargs)

        return wrapper

    return decorator


@checkargs((0, 10), (5, 15))
def test1(a, b):
    return a + b


try:
    for i, j in zip(range(0, 11), range(5, 16)):
        print(test1(i, j))
except ValueError as e:
    print(e)


def minmaxarg(func):
    min_max_val = {"min": float("inf"), "max": float("-inf")}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        all_values = [val for val in [*args, *kwargs.values()] if isinstance(val, int)]

        if all_values:
            min_max_val["min"] = min(min_max_val["min"], *all_values)
            min_max_val["max"] = max(min_max_val["max"], *all_values)

        return func(*args, **kwargs)

    wrapper.stats = min_max_val

    return wrapper


@minmaxarg
def test2(n):
    return n


test2(-10)
test2(0)
test2(10)
print(test2.stats)
