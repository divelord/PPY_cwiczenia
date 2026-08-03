"""
ZAD05

Napisz dekorator przyjmujący argument typ, który sprawdza, czy wynik funkcji jest tego typu,
jeśli nie, zgłasza wyjątek.
"""


def check_type(tp):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if not isinstance(result, tp):
                raise TypeError("Błędny typ danych")

            return result

        return wrapper

    return decorator


@check_type(int)
def add(a, b):
    return a + b


try:
    print(add(1, 2))
    print(add("a", "b"))
except TypeError as e:
    print(e)
