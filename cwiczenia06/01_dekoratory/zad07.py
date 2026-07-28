"""
ZAD07

Napisz dekorator type_check, który zapewnia, że wszystkie argumenty pozycyjne przekazane do funkcji
są typu całkowitego (int). Jeśli którykolwiek argument nie jest liczbą całkowitą,
dekorator powinien zgłosić wyjątek TypeError z odpowiednim komunikatem.
Udekorowana funkcja powinna:
• przyjmować dowolną liczbę argumentów pozycyjnych (użyj *args),
• obliczać i zwracać sumę wszystkich przekazanych argumentów.
Przykład:
• sum_all(1, 2, 3) powinno zwrócić 6
• sum_all(1, "a", 3) powinno zgłosić TypeError
"""


def type_check(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError(f"{arg} nie jest typu int")
        return func(*args, **kwargs)

    return wrapper


@type_check
def sum_all(*args):
    return sum(args)


print(sum_all(1, 2, 3))
print(sum_all(1, "a", 3))
