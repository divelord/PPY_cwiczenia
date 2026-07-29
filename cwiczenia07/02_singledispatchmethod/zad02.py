"""
ZAD02

System interakcji w stylu Minecraft
Twoim zadaniem jest zaimplementowanie uproszczonego systemu interakcji
inspirowanego grą Minecraft w Pythonie.
Utwórz klasę Player, która może wchodzić w interakcje z różnymi typami obiektów świata
za pomocą jednej metody interact(target) wykorzystującej @singledispatchmethod.
Zachowanie metody musi zależeć od typu argumentu target w czasie wykonania programu.

System musi obsługiwać następujące typy obiektów:
• Block - reprezentuje blok w świecie,
• Item - reprezentuje przedmiot możliwy do podniesienia,
• Mob - reprezentuje żywą jednostkę posiadającą punkty zdrowia.

Wymagane zachowanie:
• Jeśli celem jest Block, gracz powinien zwrócić komunikat opisujący interakcję z
blokiem.
• Jeśli celem jest Item, przedmiot powinien zostać dodany do ekwipunku gracza.
• Jeśli celem jest Mob, powinien on otrzymać obrażenia.
  Jeśli jego zdrowie spadnie do zera lub poniżej, uznaje się go za pokonanego.
• Dla nieobsługiwanych typów należy zwrócić domyślny komunikat o braku akcji.

Dodatkowe wymagania:
• Klasa Player musi przechowywać ekwipunek zebranych przedmiotów,
• Zaimplementuj __str__() do wyświetlania ekwipunku gracza,
• Zaimplementuj __len__() zwracające liczbę przedmiotów w ekwipunku.
"""
from functools import singledispatchmethod


class Block:
    def __init__(self, name):
        self.name = name


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Item({self.name})"


class Mob:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    @singledispatchmethod
    def interact(self, target):
        return f"No interaction with {target}"

    @interact.register(Block)
    def _(self, target):
        return f"{self.name} interacts with block: {target.name}"

    @interact.register(Item)
    def _(self, target):
        self.inventory.append(target)
        return f"{self.name} picked up {target.name}"

    @interact.register(Mob)
    def _(self, target):
        dmg = 10
        target.hp -= dmg

        if target.hp <= 0:
            return f"{self.name} killed {target.name}"
        return f"{self.name} hit {target.name}, HP left: {target.hp}"

    def __str__(self):
        return f"Player({self.name}, inventory={self.inventory})"

    def __len__(self):
        return len(self.inventory)


player = Player("Steve")

stone = Block("Stone")
sword = Item("Sword")
zombie = Mob("Zombie", hp=15)

print(player.interact(stone))
print(player.interact(sword))
print(player.interact(zombie))
print(player.interact(zombie))

print(player)
print(len(player))
