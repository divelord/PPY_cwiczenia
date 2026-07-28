"""
ZAD08

Napisz dekorator safe_execution, który przechwytuje wszystkie wyjątki
i wypisuje komunikat o błędzie, zamiast przerywać działanie programu.
"""


def safe_execution(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[Error]: {e}")

    return wrapper


@safe_execution
def divide(a, b):
    return a / b


divide(5, 2)
divide(5, 0)
