"""
ZAD02

Dana jest funkcja:

def slow_add(a, b):
    import time
    time.sleep(1)
    return a+b

Napisz dekorator timer, który mierzy czas wykonania tej funkcji i wypisuje go w sekundach.
Dekorator musi działać z dowolną sygnaturą funkcji.
"""

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"Czas wykonania: {end - start}")

        return result

    return wrapper


@timer
def slow_add(a, b):
    time.sleep(1)
    return a + b


print(slow_add(1, 2))
