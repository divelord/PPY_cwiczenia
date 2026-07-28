"""
ZAD04

Dana jest funkcja:

def fetch_data():
    return "data"

Napisz dwa dekoratory:
• delay(seconds) – wstrzymuje wykonanie na określoną liczbę sekund przed wywołaniem funkcji,
• timer – mierzy czas wykonania funkcji i wypisuje go w sekundach.
Następnie zastosuj oba dekoratory do funkcji fetch_data.
Ważne:
• Całkowity czas wykonania wypisany przez timer powinien uwzględniać opóźnienie.
• Dekoratory muszą działać dla dowolnej sygnatury funkcji (użyj *args oraz **kwargs).
"""

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"czas wykonania: {end - start}")

        return result

    return wrapper


def delay(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(n)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@timer
@delay(2)
def fetch_data():
    return "data"


print(fetch_data())
