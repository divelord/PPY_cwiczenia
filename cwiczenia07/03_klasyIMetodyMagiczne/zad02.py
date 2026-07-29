"""
ZAD02

Elden Ring - system walki
Zaprojektuj uproszczony system walki RPG inspirowany grą Elden Ring.
Twoim zadaniem jest zaimplementowanie systemu klas reprezentujących
postać gracza, broń oraz interakcje bojowe z wykorzystaniem metod magicznych Pythona.

Przegląd systemu:
System składa się z głównej klasy Tarnished oraz klas pomocniczych reprezentujących broń i przeciwników.

Klasa: Weapon
Reprezentuje broń używaną przez gracza.
Atrybuty:
• name (str) - nazwa broni,
• damage (int) - bazowe obrażenia.

Klasa: Enemy
Reprezentuje przeciwnika w świecie gry.
Atrybuty:
• name (str) - nazwa przeciwnika,
• hp (int) - punkty życia.

Klasa: Tarnished
Reprezentuje postać gracza.
Atrybuty:
• name (str) - nazwa gracza,
• hp (int) - punkty życia,
• weapon (Weapon | None) - aktualnie wyposażona broń.

Wymagane metody magiczne:
• __call__() → wykonuje atak na przeciwniku,
• __matmul__() → wyposaża broń przy użyciu operatora @,
• __sub__() → wykonuje unik (zmniejsza otrzymywane obrażenia),
• __len__() → zwraca aktualne HP,
• __bool__() → zwraca, czy postać żyje,
• __str__() → zwraca czytelny stan postaci.

Zasady:
• Jeśli broń nie jest wyposażona, atak zadaje minimalne obrażenia,
• HP przeciwnika zmniejsza się po ataku,
• Jeśli HP przeciwnika spadnie do 0 lub mniej, uznaje się go za pokonanego,
• Unik zmniejsza otrzymywane obrażenia zamiast odejmować pełne HP.
"""


class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


class Tarnished:
    def __init__(self, name, hp, weapon=None):
        self.name = name
        self.hp = hp
        self.weapon = weapon

    def __call__(self, target):
        dmg = self.weapon.damage if self.weapon else 10
        target.hp -= dmg
        status = f"{self.name} hits {target.name} for {dmg} damage!"

        if target.hp <= 0:
            status += f"\n{self.name} defeated {target.name}!"

        return status

    def __matmul__(self, weapon):
        if isinstance(weapon, Weapon):
            self.weapon = weapon
            return self
        return NotImplemented

    def __sub__(self, damage):
        if isinstance(damage, int):
            dmg = damage // 2
            self.hp -= dmg
            return self
        return NotImplemented

    def __len__(self):
        return self.hp

    def __bool__(self):
        return self.hp > 0

    def __str__(self):
        weapon = self.weapon.name if self.weapon else "None"
        return f"{self.name} | HP: {self.hp} | Weapon: {weapon}"


sword = Weapon("Moonveil", damage=40)
enemy = Enemy("Godrick", hp=100)

player = Tarnished("Tarnished", hp=120)
player = player @ sword

print(player(enemy))
print(len(player))
print(bool(player))
print(player)
