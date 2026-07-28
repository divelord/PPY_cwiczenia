"""
ZAD20

Utwórz klasę z prywatnym atrybutem oraz metodami getter/setter.
"""


class PrivateClass:
    def __init__(self, private_attr):
        self.__private_attr = private_attr

    def get_private_attr(self):
        return self.__private_attr

    def set_private_attr(self, newPriv):
        self.__private_attr = newPriv


priv = PrivateClass(5)
print(priv.get_private_attr())
priv.set_private_attr(10)
print(priv.get_private_attr())
