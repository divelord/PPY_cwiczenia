"""
ZAD01

Napisz dekorator uppercase, który zamienia wartość zwracaną przez funkcję (typu string) na wielkie litery.
"""


def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper


@uppercase
def to_uppercase(text):
    return text


print(to_uppercase("abc"))
print(to_uppercase("Def"))
print(to_uppercase("gHI"))
