"""
ZAD08

Dispatcher z historią
Utwórz klasę Dispatcher z metodą handle(value):
• int → podnosi do kwadratu,
• str → odwraca napis,
• list → odwraca listę.

Dodatkowo:
• Przechowuj historię operacji,
• Zaimplementuj __getitem__(), aby uzyskać dostęp do historii przez indeks.
"""
from functools import singledispatchmethod


class Dispatcher:
    def __init__(self):
        self.history = []

    @singledispatchmethod
    def handle(self, value):
        result = "Unknown type"
        self.history.append(result)

        return result

    @handle.register(int)
    def _(self, value):
        result = value ** 2
        self.history.append(result)

        return result

    @handle.register(str)
    def _(self, value):
        result = value[::-1]
        self.history.append(result)

        return result

    @handle.register(list)
    def _(self, value):
        result = value[::-1]
        self.history.append(result)

        return result

    def __getitem__(self, index):
        return self.history[index]


dispatcher = Dispatcher()

dispatcher.handle(10.5)
dispatcher.handle(10)
dispatcher.handle("abc")
dispatcher.handle([1, 2, 3])

print(dispatcher.history)
print(dispatcher.history[1])
