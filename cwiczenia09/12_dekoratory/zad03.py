"""
ZAD03

Napisz dekorator przyjmujący argument tekstowy prefix, który powoduje,
że przed każdym wynikiem funkcji zostaje dodany ten prefix.
"""


def add_prefix(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            return prefix + result

        return wrapper

    return decorator


@add_prefix(":D ")
def add_suffix(suffix):
    return suffix


print(add_suffix('abc'))
