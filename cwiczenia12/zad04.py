"""
ZAD04

Utwórz klasę Interval, której obiekty reprezentują przedziały
[a,b] na osi liczbowej.

Końce przedziału a oraz b powinny zostać zaimplementowane
jako prywatne właściwości bez setterów.

Użyj dekoratora @functools.total_ordering, aby zaimplementować
wszystkie sześć operatorów porównania. „Mniejszym” przedziałem jest ten
o mniejszej współrzędnej a, a jeśli są one równe - o mniejszej współrzędnej b.

Jeśli obj jest obiektem tej klasy, to len(obj) powinno zwracać
długość przedziału reprezentowanego przez obj.

Wywołanie
    obj1.intersects(obj2)
powinno zwracać True wtedy i tylko wtedy, gdy dwa przedziały mają niepuste przecięcie.

Wyrażenie
    obj1 | obj2
powinno zwracać obiekt reprezentujący najmniejszy przedział zawierający zarówno obj1, jak i obj2.

Wyrażenie
    obj1 & obj2
powinno zwracać obiekt reprezentujący część wspólną dwóch przedziałów
albo zgłaszać wyjątek ValueError, jeśli przedziały nie przecinają się.

Zapewnij sensowną i zwięzłą reprezentację tekstową obiektów tej klasy.
"""
import functools


@functools.total_ordering
class Interval:
    def __init__(self, a, b):
        if a > b:
            a, b = b, a

        self.__a = a
        self.__b = b

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    def __len__(self):
        return self.__b - self.__a

    def __eq__(self, other):
        return self.__a == other.__a and self.__b == other.__b

    def __lt__(self, other):
        if self.__a == other.__a:
            return self.__b < other.__b
        return self.__a < other.__a

    def intersects(self, other):
        return max(self.__a, other.__a) <= min(self.__b, other.__b)

    def __or__(self, other):
        return Interval(min(self.__a, other.__a), max(self.__b, other.__b))

    def __and__(self, other):
        if not self.intersects(other):
            raise ValueError("Intervals do not intersect.")
        return Interval(max(self.__a, other.__a), min(self.__b, other.__b))

    def __str__(self):
        return f"[{self.__a}, {self.__b}]"

    def __repr__(self):
        return self.__str__()


i1, i2, i3 = Interval(2, 7), Interval(-4, 4), Interval(-8, 1)

print('Intervals:', i1, i2, i3)
print('Lengths: ', len(i1), len(i2), len(i3))

print('i1 & i2, i1 & i3, i2 & i3 exist?',
      i1.intersects(i2),
      i1.intersects(i3),
      i2.intersects(i3))

print('i1&i2 = ', i1 & i2, ' i2&i3 = ', i2 & i3)

print('i1|i2 = ', i1 | i2,
      ' i1|i3 = ', i1 | i3,
      ' i2|i3 = ', i2 | i3)

lst = [i1, i2, i3]

print('Unsorted: ', lst)

lst.sort()

print('Sorted: ', lst)
