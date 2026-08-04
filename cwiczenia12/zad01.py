"""
ZAD01

Utwórz niewielki system inspirowany grą Devil May Cry 5.

Zaimplementuj następujące klasy:
• Demon- klasa bazowa opisująca demony.
• LesserDemon oraz BossDemon dziedziczące po Demon.
• Weapon- klasa opisująca broń.
• HalfDemon- klasa opisująca półdemonicznych łowców.
• Dante dziedzicząca po HalfDemon.

Każdy obiekt klasy Demon powinien zawierać:
• nazwę demona,
• punkty życia,
• siłę ataku.

Każdy obiekt klasy Weapon powinien zawierać:
• nazwę broni,
• obrażenia,
• typ broni.

Każdy obiekt klasy HalfDemon powinien zawierać:
• nazwę postaci,
• punkty życia,
• rangę stylu,
• listę broni.

Zaimplementuj następującą funkcjonalność:
• Metoda attack(enemy) zmniejsza liczbę punktów życia przeciwnika.
• Metoda add_weapon(weapon) dodaje broń do listy broni.
• Metoda remove_weapon(name) usuwa broń o podanej nazwie.
• Przeciąż operator + tak, aby:
        half_demon + weapon
    dodawało broń do ekwipunku postaci.
• Przeciąż funkcję len() dla klasy HalfDemon tak, aby:
        len(character)
    zwracało liczbę posiadanych broni.
• Zaimplementuj metodę __str__ dla wszystkich klas.
• Zaimplementuj metodę __contains__ w klasie HalfDemon tak, aby:
        "Rebellion" in dante
    zwracało True, jeśli Dante posiada broń o tej nazwie.

Dodatkowo utwórz klasę DemonFactory implementującą wzorzec projektowy Factory.

Fabryka powinna zawierać statyczne metody:
    create_lesser_demon(name)
    create_boss_demon(name)

Fabryka automatycznie przypisuje domyślne statystyki w zależności od typu demona.
Na przykład:
• Mniejsze demony:
    – HP=50
    – ATK =10
• Bossowie:
    – HP=300
    – ATK =50
"""


class Demon:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def __str__(self):
        return f"{self.__class__.__name__}({self.name}, HP={self.hp}, ATK={self.atk})"


class LesserDemon(Demon):
    pass


class BossDemon(Demon):
    pass


class Weapon:
    def __init__(self, name, dmg, weapon_type):
        self.name = name
        self.dmg = dmg
        self.weapon_type = weapon_type

    def __str__(self):
        return f"Weapon({self.name}, DMG={self.dmg}, type={self.weapon_type})"


class HalfDemon:
    def __init__(self, name, hp, rank):
        self.name = name
        self.hp = hp
        self.rank = rank
        self.weapons = []

    def attack(self, enemy):
        dmg = self.weapons[0].dmg if self.weapons else 10
        enemy.hp = max(0, enemy.hp - dmg)

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def remove_weapon(self, weapon):
        for w in self.weapons:
            if w.name == weapon:
                self.weapons.remove(w)
                break

    def __add__(self, weapon):
        self.weapons.append(weapon)
        return self

    def __len__(self):
        return len(self.weapons)

    def __str__(self):
        weapon_text = "\n".join([f"- {w.name}" for w in self.weapons])
        return f"{self.__class__.__name__}(HP={self.hp}, Rank={self.rank})\nWeapons:\n{weapon_text}"

    def __contains__(self, weapon):
        return any(w.name == weapon for w in self.weapons)


class Dante(HalfDemon):
    pass


class DemonFactory:
    @staticmethod
    def create_lesser_demon(name):
        return LesserDemon(name, 50, 10)

    @staticmethod
    def create_boss_demon(name):
        return BossDemon(name, 300, 50)


rebellion = Weapon("Rebellion", 45, "Sword")
ebony = Weapon("Ebony", 20, "Pistol")

dante = Dante("Dante", 250, "SSS")

dante.add_weapon(rebellion)

dante = dante + ebony

print(dante)

print(len(dante))

print("Rebellion" in dante)
print("Yamato" in dante)

enemy1 = DemonFactory.create_lesser_demon("Empusa")
enemy2 = DemonFactory.create_boss_demon("Urizen")

print(enemy1)
print(enemy2)

dante.attack(enemy1)

print(enemy1)
