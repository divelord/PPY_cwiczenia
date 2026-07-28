"""
ZAD09

Napisz dekorator auth_required, który pozwala wykonać funkcję tylko wtedy,
gdy przekazano argument nazwany user="admin".
"""


def auth_required(func):
    def wrapper(*args, **kwargs):
        if kwargs.get("user") == "admin":
            return func(*args, **kwargs)
        else:
            return "Admin required"

    return wrapper


@auth_required
def test(user=""):
    return "test"


print(test())
print(test(user="admin"))
print(test(user="xyz"))
