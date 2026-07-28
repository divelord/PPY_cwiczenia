"""
ZAD01

Napisz dekorator memorize, który buforuje wyniki funkcji dla danych argumentów.
• Dekorator powinien działać dla dowolnej sygnatury funkcji.
• Powtórne wywołania z tymi samymi argumentami powinny zwracać zapisany wynik.
"""

import functools


def memorize(func):
    dic = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key not in dic:
            dic[key] = func(*args, **kwargs)

        return dic[key]

    return wrapper


@memorize
def add(a, b):
    print(f"Computing {a} + {b}...")
    return a + b


print(add(2, 3))
print(add(2, 3))
print(add(3, 4))
