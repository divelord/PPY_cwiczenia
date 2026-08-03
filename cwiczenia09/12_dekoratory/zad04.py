"""
ZAD04

Napisz dekorator przyjmujący argument limit, który blokuje wykonanie funkcji,
jeśli liczba wywołań przekroczy limit.
"""


def add_limit(limit):
    def decorator(func):
        call_count = 0

        def wrapper(*args, **kwargs):
            nonlocal call_count

            if call_count < limit:
                call_count += 1

                return func(*args, **kwargs)

            return None

        return wrapper

    return decorator


@add_limit(5)
def print_hello(value):
    return f"Hello {value}"


for i in range(10):
    print(print_hello(i))
