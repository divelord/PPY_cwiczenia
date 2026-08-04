"""
ZAD02

Utwórz hierarchię klas opisującą postacie oraz pojazdy z gry Lego Batman.

Zaimplementuj następujące klasy:
• Character - klasa bazowa zawierająca:
    – nazwę postaci,
    – punkty życia,
    – siłę ataku.
• Hero oraz Villain dziedziczące po Character.
• Batman, Robin oraz Joker jako klasy potomne powyższych klas.
• Vehicle - klasa zawierająca:
    – nazwę pojazdu,
    – prędkość,
    – wytrzymałość.
• Batmobile dziedzicząca zarówno po Batman, jak i po Vehicle.

Klasy powinny obsługiwać następującą funkcjonalność:
• Przeciąż operator + tak, aby:
        character + number
    zwiększało liczbę punktów życia postaci.
• Przeciąż operator - tak, aby:
        character - number
    zmniejszało liczbę punktów życia, ale liczba punktów życia nie może spaść poniżej zera.
• Przeciąż operator > tak, aby silniejsze postacie były uznawane za większe.
  Siła postaci jest definiowana jako:
        health_points + attack_power
• Zaimplementuj metodę __str__ wyświetlającą zwięzłe informacje o obiektach.
• Zaimplementuj metodę __len__ dla klasy Vehicle, zwracającą jej wytrzymałość.
• Zaimplementuj metodę attack(other) zmniejszającą liczbę punktów życia przeciwnika.
• Dodaj zmienną klasową zliczającą liczbę utworzonych postaci.

Dodatkowo:
• Zastosuj wielodziedziczenie w klasie Batmobile.
• Wypisz MRO (Batmobile.__mro__) i wyjaśnij, dlaczego klasy pojawiają się w tej kolejności.
"""


class Character:
    character_count = 0

    def __init__(self, character_name, hp, atk):
        self.character_name = character_name
        self.hp = hp
        self.atk = atk
        Character.character_count += 1

    def __add__(self, number):
        self.hp += number
        return self

    def __sub__(self, number):
        self.hp = max(0, self.hp - number)
        return self

    def __gt__(self, other):
        return (self.hp + self.atk) > (other.hp + other.atk)

    def __str__(self):
        return f"{self.__class__.__name__}(HP={self.hp}, ATK={self.atk})"

    def attack(self, other):
        other.hp = max(0, other.hp - self.atk)


class Hero(Character):
    pass


class Villain(Character):
    pass


class Batman(Hero):
    pass


class Robin(Hero):
    pass


class Joker(Villain):
    pass


class Vehicle:
    def __init__(self, vehicle_name, speed, durability):
        self.vehicle_name = vehicle_name
        self.speed = speed
        self.durability = durability

    def __str__(self):
        return f"{self.__class__.__name__}({self.vehicle_name}, speed={self.speed}, durability={self.durability})"

    def __len__(self):
        return self.durability


class Batmobile(Batman, Vehicle):
    def __init__(self, character_name, hp, atk, vehicle_name, speed, durability):
        Batman.__init__(self, character_name, hp, atk)
        Vehicle.__init__(self, vehicle_name, speed, durability)

    def __str__(self):
        return f"{self.__class__.__name__}({self.vehicle_name}, speed={self.speed}, durability={self.durability})"


batman = Batman("Batman", 120, 35)
joker = Joker("Joker", 90, 25)

print(batman)
print(joker)

batman.attack(joker)

print(joker)

joker = joker + 20

print(joker)

print(batman > joker)

batmobile = Batmobile(
    "Batman",
    150,
    40,
    "Tumbler",
    320,
    500
)

print(batmobile)

print(len(batmobile))

for obj in Batmobile.__mro__:
    print(obj)

"""
Najpierw wyświetla klasę Batmobile, ponieważ jest to wywoływana klasa wyjściowa.
Następnie wyświetla klasę Batman, ponieważ została podana jako pierwsza podczas definiowania klasy.
Następnie klasy po, których dziedziczy klasa Batman (Hero -> Character).
Następnie klasa Vehicle, ponieważ została jako druga zdefiniowana w klasie Batmobile.
Na samym końcu klasa object, ponieważ po tej klasie dziedziczą wszystkie klasy.
"""
