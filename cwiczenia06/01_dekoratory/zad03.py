"""
ZAD03

Dana jest funkcja:

def greet(name):
    print(f"Hello {name}")

Napisz dekorator repeat(n), który powoduje, że funkcja zostaje wykonana n razy.
"""


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(5)
def greet(name):
    print(f"Hello {name}")


greet("XYZ")
