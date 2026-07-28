"""
ZAD10

Napisz dekorator retry(n), który ponawia wykonanie funkcji maksymalnie n razy
w przypadku wystąpienia wyjątku.
"""


def retry(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(1, n + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"[Error #{i}]: {e}")
            return None

        return wrapper

    return decorator


@retry(5)
def divide(a, b):
    return a / b


divide(5, 0)
