"""
ZAD03

Dynamiczna klasa sumująca
Twoim zadaniem jest stworzenie klasy o nazwie SmartAdder.
Klasa ta powinna działać jak elastyczny kontener, który przechowuje różne typy danych na różne sposoby.
Wewnątrz klasy zaimplementuj metodę add(value).
Metoda ta musi wykorzystywać @singledispatchmethod, dzięki czemu automatycznie będzie reagować inaczej
w zależności od typu przekazanej wartości.

Zachowanie metody add(value):
• Jeśli value jest typu int, dodaj ją do wewnętrznego licznika liczbowego.
• Jeśli value jest typu list, rozszerz wewnętrzną listę o jej elementy.
• Jeśli value jest typu str, dołącz ją do wewnętrznego napisu.
Zamiast używać wielu instrukcji if, metoda powinna automatycznie wybierać odpowiednie zachowanie
na podstawie typu danych wejściowych.

Dodatkowo klasa musi obsługiwać:
• __str__()- zwraca czytelny opis aktualnego stanu (licznik, lista, zawartość napisu),
• __len__()- zwraca łączną liczbę przechowywanych elementów
  (np. liczba do danych liczb + liczba elementów listy + liczba znaków w napisie).
"""
from functools import singledispatchmethod


class SmartAdder:
    def __init__(self):
        self.counter = 0
        self.lst = []
        self.text = ""

    @singledispatchmethod
    def add(self, value):
        print("Unsupported")

    @add.register(int)
    def _(self, value):
        self.counter += value

    @add.register(list)
    def _(self, value):
        self.lst.extend(value)

    @add.register(str)
    def _(self, value):
        self.text += value + " "

    def __str__(self):
        return f"{self.counter}, {self.lst}, {self.text}"

    def __len__(self):
        return self.counter + len(self.lst) + len(self.text)


smart_adder = SmartAdder()

smart_adder.add(10)
smart_adder.add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
smart_adder.add("abc def ghi")
smart_adder.add(13)
smart_adder.add([4, 32, 4, 2, 35])
smart_adder.add("adfs")

print(smart_adder)
print(len(smart_adder))
