"""
ZAD01

Celem zadania jest zaprojektowanie i implementacja systemu symulującego walkę
pomiędzy czarodziejami z wykorzystaniem:
• programowania obiektowego (klasy i metody),
• generatorów,
• mechanizmu iteracji.

Zaimplementuj następujące klasy:
- Klasa Attack
    Powinna zawierać:
    • nazwę ataku (name),
    • bazowe obrażenia (damage).
-Klasa Wizard
    Powinna zawierać:
    • imię (name),
    • punkty życia (hp),
    • listę dostępnych ataków (attacks).
    Metody:
    • add_attack(attack) — dodaje atak do listy,
    • is_alive() — zwraca wartość logiczną informującą, czy hp > 0,
    • attack(opponent):
        – losuje atak z dostępnych,
        – zmniejsza punkty życia przeciwnika,
        – zwraca opis tekstowy wykonanej akcji.

Generator walki
Zaimplementuj funkcję generatora:
def fight(wizard1, wizard2):
Wymagania:
• walka odbywa się w turach (naprzemiennie),
• każda tura powinna być zwracana przez yield,
• generator kończy działanie po przegranej jednego z czarodziejów,
• ostatnia wartość zwrócona przez yield powinna zawierać informację o wyniku walki.

Użycie generatora
• uruchom walkę przy użyciu pętli for,
• wyświetl przebieg walki w konsoli.
Dodaj atrybuty:
• strength — zwiększa obrażenia,
• defense — redukuje obrażenia,
• agility — szansa na unik.
Dodaj:
• możliwość uniku,
• możliwość blokowania obrażeń,
• losowy mnożnik obrażeń.
Dodaj efekty:
• stunned — pomija turę,
• burning — zadaje obrażenia co turę.
Zaimplementuj generator tworzący losowe statystyki postaci.

Turniej (iterator)
Zaimplementuj klasę:
class Tournament:
    def __iter__(self):
Wymagania:
• iteruje po kolejnych walkach,
• zwraca wyniki walk.

Wymagania techniczne
• należy użyć generatora (yield),
• należy zastosować klasy i metody,
• kod powinien być czytelny i modularny.

Wskazówki
• generator nie wykonuje się bez iteracji,
• można użyć random.choice() do wyboru ataku,
• do testowania można użyć for lub next().

Efekt końcowy
Program powinien umożliwiać:
• tworzenie czarodziejów,
• przeprowadzenie walki,
• obserwację przebiegu walki krok po kroku.
"""

import random


def stats_generator():
    while True:
        yield {
            "hp": random.randint(300, 400),
            "strength": random.randint(1, 50),
            "defense": random.randint(1, 25),
            "agility": random.randint(1, 25),
        }


get_stats = stats_generator()


class Attack:
    def __init__(self, name, damage, effect=None, effect_chance=0.0):
        self.name = name
        self.damage = damage
        self.effect = effect
        self.effect_chance = effect_chance


class Wizard:
    def __init__(self, name, attacks):
        self.name = name
        self.attacks = attacks

        stats = next(get_stats)
        self.hp = stats['hp']
        self.max_hp = self.hp
        self.strength = stats['strength']
        self.defense = stats['defense']
        self.agility = stats['agility']

        self.is_burning = False
        self.burn_count = 0
        self.is_frozen = False
        self.freeze_count = 0
        self.is_stunned = False

    def add_attack(self, attack):
        self.attacks.append(attack)

    def is_alive(self):
        return self.hp > 0

    def reset_stats(self):
        self.hp = self.max_hp
        self.is_burning = False
        self.burn_count = 0
        self.is_frozen = False
        self.freeze_count = 0
        self.is_stunned = False

    def attack(self, opponent):
        spell = random.choice(self.attacks)

        description = f"{self.name} użył zaklęcia {spell.name} na {opponent.name}\n"

        if not (opponent.is_frozen or opponent.is_stunned):
            if random.randint(1, 100) < opponent.defense:
                description += f"{opponent.name} zablokował zaklęcie {spell.name}\n"
                return description
            if random.randint(1, 100) < opponent.agility:
                description += f"{opponent.name} uniknął zaklęcia {spell.name}\n"
                return description

        multiplier = random.uniform(0.5, 1.5)
        dmg = round((spell.damage + self.strength / 10) * multiplier, 2)
        opponent.hp = round(opponent.hp - dmg, 2)

        description += f"Zaklęcie zadało {dmg} DMG\n"

        if spell.effect and random.random() < spell.effect_chance:
            if spell.effect == "burning" and not opponent.is_burning:
                opponent.burn_count = 0
                opponent.is_burning = True
                description += f"{opponent.name} zaczął płonąć\n"
            elif spell.effect == "freeze" and not opponent.is_frozen:
                opponent.freeze_count = 0
                opponent.is_frozen = True
                description += f"{opponent.name} został zamrożony\n"
            elif spell.effect == "stun" and not opponent.is_stunned:
                opponent.is_stunned = True
                description += f"{opponent.name} został ogłuszony\n"

        description += f"{opponent.name} ma {max(0, round(opponent.hp, 2))}HP\n"

        return description


def fight(wizard1, wizard2):
    wizard1.reset_stats()
    wizard2.reset_stats()

    turn = True

    yield "\n=================================="
    yield f"{wizard1.name} vs {wizard2.name}"
    yield "==================================\n"

    while wizard1.is_alive() and wizard2.is_alive():
        attacker = wizard1 if turn else wizard2
        defender = wizard2 if turn else wizard1

        if attacker.is_burning:
            attacker.burn_count += 1
            burn_dmg = 10
            attacker.hp = round(attacker.hp - burn_dmg, 2)

            yield (f"Ogień zadaje {burn_dmg} DMG czarodziejowi {attacker.name}\n"
                   f"{attacker.name} ma teraz {max(0, round(attacker.hp, 2))}hp \n")

            if attacker.burn_count >= 3:
                attacker.is_burning = False
                attacker.burn_count = 0
                yield f"{attacker.name} przestał płonąć\n"

            if not attacker.is_alive():
                break

        if attacker.is_frozen:
            attacker.freeze_count += 1

            yield f"{attacker.name} jest zamrożony i mija turę\n"

            if attacker.freeze_count >= 2:
                attacker.is_frozen = False
                attacker.freeze_count = 0
                yield f"{attacker.name} odmroził się\n"

            turn = not turn
            continue

        if attacker.is_stunned:
            attacker.is_stunned = False

            yield f"{attacker.name} jest ogłuszony\n"

            turn = not turn
            continue

        yield attacker.attack(defender)

        turn = not turn

    winner = wizard1 if wizard1.is_alive() else wizard2

    yield f"Wygrywa {winner.name}"


class Tournament:
    def __init__(self, wizards):
        self.wizards = wizards

    def __iter__(self):
        alive_wizards = list(self.wizards)
        round_number = 1

        while len(alive_wizards) > 1:
            yield f"\nRUNDA {round_number}"
            winners = []

            for wizard in range(0, len(alive_wizards) - 1, 2):
                wizard1 = alive_wizards[wizard]
                wizard2 = alive_wizards[wizard + 1]

                for battle in fight(wizard1, wizard2):
                    yield battle

                battle_winner = wizard1 if wizard1.is_alive() else wizard2
                winners.append(battle_winner)

            if len(alive_wizards) % 2 != 0:
                lucky_wizard = alive_wizards[-1]
                winners.append(lucky_wizard)

                yield f"\nZ Powodu braku pary do walki {lucky_wizard.name} przechodzi dalej"

            alive_wizards = winners
            round_number += 1

        yield f"\nNajwiększym czarodziejem zostaje: {alive_wizards[0].name}"


fireBall = Attack("FireBall", 50, "burning", 0.25)
iceLance = Attack("IceLance", 35, "freeze", 0.3)
lightningStrike = Attack("LightningStrike", 45, "stun", 0.4)
windCutter = Attack("WindCutter", 25)

allSpells = [fireBall, iceLance, lightningStrike, windCutter]

gandalf = Wizard("Gandalf", random.sample(allSpells, 3))
saruman = Wizard("Saruman", random.sample(allSpells, 3))
dumbledore = Wizard("Dumbledore", random.sample(allSpells, 3))
voldemort = Wizard("Voldemort", random.sample(allSpells, 3))
merlin = Wizard("Merlin", random.sample(allSpells, 3))

wizards = [gandalf, saruman, dumbledore, voldemort, merlin]
random.shuffle(wizards)

print("============================================")
print("Pojedyncza walka")
print("============================================")
for battle_turn in fight(gandalf, dumbledore):
    print(battle_turn)
print()
print("============================================")
print("Turniej")
print("============================================")
for battle in Tournament(wizards):
    print(battle)
