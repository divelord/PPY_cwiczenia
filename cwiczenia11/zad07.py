"""
ZAD07

Utwórz klasę Book zawierającą:
• atrybuty: title, author,
• metodę klasową fromTuple(data), która tworzy obiekt książki z krotki.

Przykład:
b = Book.fromTuple(("Dune", "Frank Herbert"))
"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def fromTuple(cls, data):
        return cls(*data)


b = Book.fromTuple(("Dune", "Frank Herbert"))

print(b.title)
print(b.author)
