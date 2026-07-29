"""
ZAD07

Łączenie danych
Utwórz klasę Merger z metodą merge(value):
• list → rozszerza wewnętrzną listę,
• set → wykonuje sumę zbiorów (unię) z wewnętrznym zbiorem,
• dict → łączy słowniki.

Dodatkowo:
• Zaimplementuj __add__(), aby można było łączyć dwa obiekty typu Merger,
• Zaimplementuj __str__().
"""
from functools import singledispatchmethod


class Merger:
    def __init__(self):
        self.list_data = []
        self.set_data = set()
        self.dict_data = {}

    @singledispatchmethod
    def merge(self, value):
        print("Unknown type")

    @merge.register(list)
    def _(self, value):
        self.list_data.extend(value)

    @merge.register(set)
    def _(self, value):
        self.set_data.update(value)

    @merge.register(dict)
    def _(self, value):
        self.dict_data.update(value)

    def __add__(self, other):
        if not isinstance(other, Merger):
            raise TypeError

        new_merger = Merger()

        new_merger.merge(self.list_data)
        new_merger.merge(other.list_data)

        new_merger.merge(self.set_data)
        new_merger.merge(other.set_data)

        new_merger.merge(self.dict_data)
        new_merger.merge(other.dict_data)

        return new_merger

    def __str__(self):
        return f"{self.list_data}\n{self.set_data}\n{self.dict_data}"


merger1 = Merger()

merger1.merge([1, 2])
merger1.merge([3, 4])

merger1.merge({1, 2})
merger1.merge({3, 4})

merger1.merge({"a": 1})
merger1.merge({"b": 2})

print(merger1)

merger2 = Merger()

merger2.merge([5, 6])
merger2.merge([7, 8])

merger2.merge({5, 6})
merger2.merge({7, 8})

merger2.merge({"c": 1})
merger2.merge({"d": 2})

print(merger2)

print(merger1 + merger2)
