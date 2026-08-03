"""
ZAD02

Napisz dekorator, który blokuje wykonanie funkcji, jeśli liczba przekazanych argumentów pozycyjnych
jest mniejsza niż 2 (w takim przypadku zwróć None).
"""


def block(func):
    def wrapper(*args, **kwargs):
        if len(args) < 2:
            return None
        return func(*args, **kwargs)

    return wrapper


@block
def add(a, b):
    return a + b


print(add(1))
print(add(1, 2))
