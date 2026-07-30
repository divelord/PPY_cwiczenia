"""
ZAD10

Napisz dekorator, który zgłasza wyjątek WrongFilePath,
gdy podana nazwa pliku nie kończy się na ’.txt’.
"""
from exceptions import WrongFilePath


def check_for_file(func):
    def wrapper(path):
        if not path.endswith(".txt"):
            raise WrongFilePath(path)
        return func(path)

    return wrapper


@check_for_file
def check_file(path):
    print(f"Dobry format pliku")


try:
    check_file("../THE_HOBBIT.txt")
    check_file("zad10.py")
except WrongFilePath as e:
    print(e)
