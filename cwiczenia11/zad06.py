"""
ZAD06

Utwórz klasę Machine zawierającą:
• atrybuty instancji: name (napis) oraz power (int),
• atrybut klasowy machineCount, przechowujący liczbę utworzonych maszyn.

Za każdym razem, gdy tworzona jest nowa maszyna, zaktualizuj liczbę maszyn.

Dodaj metodę klasową:
    displayCount()
która wyświetla liczbę aktualnie istniejących maszyn.

Następnie utwórz klasę pochodną Android, dziedziczącą po Machine.
Klasa Android powinna dodatkowo przechowywać:
• type (napis),
• number (int),
• id(napis– numer+typ). Przy każdym dodaniu identyfikatora należy sprawdzić, czy jest on unikalny.

Sprawdź, czy licznik maszyn działa poprawnie dla obu klas.

Wskazówki:
• Użyj type(self).machineCount += 1.
• Użyj super() wewnątrz konstruktora klasy pochodnej.
• Metoda klasowa powinna korzystać z cls.
"""


class Machine:
    machineCount = 0

    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power
        type(self).machineCount += 1

    @classmethod
    def displayCount(cls):
        return cls.machineCount


class Android(Machine):
    machineCount = 0
    android_ids = set()

    def __init__(self, name: str, power: int, type: str, number: int):
        super().__init__(name, power)
        self.type = type
        self.number = number

        android_id = f"{number}{type}"

        if android_id in Android.android_ids:
            raise ValueError(f"Android o ID {android_id} już istnieje")

        Android.android_ids.add(android_id)

        self.id = android_id


m1 = Machine("m1", 1)

print(Machine.displayCount())

a1 = Android("a1", 1, "b", 10)
a2 = Android("a2", 1, "c", 20)

print(Machine.displayCount())
print(Android.displayCount())

m2 = Machine("m2", 2)

print(Machine.displayCount())
print(Android.displayCount())
