"""
ZAD01

Alice: Madness Returns - System interakcji
Zaprojektuj uproszczony system interakcji inspirowany grą Alice: Madness Returns.
Twoim zadaniem jest zaimplementowanie klasy Player, która może wchodzić
w interakcje z różnymi obiektami w świecie za pomocą jednej metody interact(target)
wykorzystującej @singledispatchmethod.
Zachowanie metody musi zależeć od typu argumentu target.

Obsługiwane typy interakcji:
• Cake - zwiększa rozmiar Alice,
• Potion - zmniejsza rozmiar Alice,
• HobbyHorse - podniesienie broni,
• PepperGrinder - podniesienie broni,
• VorpalBlade - podniesienie broni.

Wymagane zachowanie:
• Alice musi posiadać wewnętrzny atrybut size,
• Interakcja z Cake zwiększa rozmiar Alice,
• Interakcja z Potion zmniejsza rozmiar Alice,
• Interakcja z broniami (HobbyHorse, PepperGrinder, VorpalBlade) wyposaża Alice w broń,
• Nieobsługiwane typy powinny zwracać domyślny komunikat o braku interakcji.

Dodatkowe wymagania:
• Zaimplementuj __str__() do wyświetlania aktualnego stanu Alice,
• Zaimplementuj __len__() zwracające aktualny rozmiar Alice,
• Zaimplementuj __bool__() określające, czy Alice jest nadal stabilna (rozmiar > 0).

Oczekiwane zachowanie (przykład):
• Cake zwiększa rozmiar Alice,
• Potion zmniejsza rozmiar Alice,
• Broń zmienia aktualnie wyposażony przedmiot.
"""
from functools import singledispatchmethod


class Cake: pass


class Potion: pass


class HobbyHorse: pass


class PepperGrinder: pass


class VorpalBlade: pass


class Alice:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.weapon = None

    @singledispatchmethod
    def interact(self, target):
        return f"{self.name} cannot interact with {target}"

    @interact.register(Cake)
    def _(self, target):
        self.size += 5
        return f"After using {target.__class__.__name__} {self.name} grew larger"

    @interact.register(Potion)
    def _(self, target):
        self.size -= 5
        return f"After using {target.__class__.__name__} {self.name} grew smaller"

    @interact.register(HobbyHorse)
    @interact.register(PepperGrinder)
    @interact.register(VorpalBlade)
    def _(self, target):
        self.weapon = target.__class__.__name__
        return f"{self.name} equipped {self.weapon}"

    def __str__(self):
        return f"{self.name} with size {self.size} and weapon {self.weapon}"

    def __len__(self):
        return self.size

    def __bool__(self):
        return self.size > 0


alice = Alice("Alice", size=10)

cake = Cake()
potion = Potion()

horse = HobbyHorse()
grinder = PepperGrinder()
blade = VorpalBlade()

print(alice.interact(cake))
print(alice.interact(potion))

print(alice.interact(horse))
print(alice.interact(grinder))
print(alice.interact(blade))

print(alice)
print(len(alice))
print(bool(alice))
