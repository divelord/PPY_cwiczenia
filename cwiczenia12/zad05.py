"""
ZAD05

Utwórz klasę Peekable, której konstruktor przyjmuje obiekt iterowalny.

Obiekt tej klasy powinien sam być iterowalny (tj. implementować __iter__ oraz __next__),
a iteracja po nim powinna zwracać elementy przekazanego obiektu iterowalnego.

Dodatkowo metoda peek powinna umożliwiać podejrzenie następnego elementu bez jego pobierania.
"""


class Peekable:
    def __init__(self, iterable):
        self._iterator = iter(iterable)
        self._next_item = None
        self._has_next = False

    def __iter__(self):
        return self

    def __next__(self):
        if self._has_next:
            item = self._next_item
            self._next_item = None
            self._has_next = False
            return item
        return next(self._iterator)

    def peek(self):
        if not self._has_next:
            self._next_item = next(self._iterator)
            self._has_next = True
        return self._next_item


peekable = Peekable([1, 2, 3, 4, 5])

print(peekable.peek(), end=' ')
print(next(peekable), end=' ')

print(peekable.peek(), end=' ')
print(peekable.peek(), end=' ')

print(next(peekable), end=' ')
print(peekable.peek(), end=' ')

print('\nAnd the rest...')

for e in peekable:
    print(e)
