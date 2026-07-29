"""
ZAD01

NieR: Automata - system walki
Zaprojektuj uproszczony system walki inspirowany grą NieR: Automata.
Twoim zadaniem jest zaimplementowanie zestawu klas reprezentujących androidy bojowe
oraz system wykonywania ataków z wykorzystaniem metod magicznych Pythona.

Przegląd systemu:
System składa się z jednej klasy jednostki bojowej YoRHaUnit oraz dwóch klas pomocniczych
wykorzystywanych do łączonych i wzmocnionych ataków.

Klasa: YoRHaUnit
Reprezentuje pojedynczego androida bojowego.
Atrybuty:
• name (str) - identyfikator jednostki,
• energy (int) - poziom energii / wytrzymałości,
• damage (int) - bazowa siła ataku.
Wymagane metody:
• __call__() - wykonuje atak i zmniejsza energię,
• __add__() - łączy dwie jednostki w system wspólnego ataku,
• __mul__() - zwraca wzmocnioną wersję jednostki lub systemu (tryb overclock),
• __len__() - zwraca aktualny poziom energii,
• __bool__() - zwraca, czy jednostka jest aktywna (energia > 0),
• __str__() - zwraca czytelny stan jednostki.

Klasa: CompositeSystem
Reprezentuje połączony system ataku utworzony z wielu jednostek.
Atrybuty:
• units (list[YoRHaUnit]) - lista jednostek uczestniczących.
Wymagane metody:
• __call__() - wykonuje ataki dla wszystkich jednostek w systemie,
• __mul__() - tworzy wzmocnioną wersję systemu.

Klasa: BoostedUnit
Reprezentuje tymczasowo wzmocnioną (przetaktowaną) pojedynczą jednostkę.
Atrybuty:
• unit (YoRHaUnit) - opakowana jednostka,
• factor (int) - mnożnik obrażeń.
Wymagane metody:
• __call__() - wykonuje wzmocniony atak,
• __len__() - zwraca energię jednostki,
• __bool__() - zwraca, czy jednostka jest aktywna.

Klasa: BoostedSystem
Reprezentuje tymczasowo wzmocnioną grupę jednostek.
Atrybuty:
• units (list[YoRHaUnit]) - lista jednostek,
• factor (int) - globalny mnożnik obrażeń.
Wymagane metody:
• __call__() - wykonuje wzmocnione ataki wszystkich jednostek,
• __len__() - zwraca sumaryczną energię wszystkich jednostek,
• __bool__() - zwraca, czy przynajmniej jedna jednostka jest aktywna.
"""


class YoRHaUnit:
    def __init__(self, name, energy, damage):
        self.name = name
        self.energy = energy
        self.damage = damage

    def __call__(self):
        if self.energy > 0:
            self.energy -= 10
            return f"{self.name} ATTACK!"
        return f"{self.name} out of energy!"

    def __add__(self, other):
        if isinstance(other, YoRHaUnit):
            return CompositeSystem([self, other])
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return BoostedUnit(self, other)
        return NotImplemented

    def __len__(self):
        return self.energy

    def __bool__(self):
        return self.energy > 0

    def __str__(self):
        status = "ACTIVE" if self.energy > 0 else "INACTIVE"
        return f"{self.name} | HP: {self.energy} | DMG: {self.damage} | {status}"


class CompositeSystem:
    def __init__(self, units):
        self.units = units

    def __call__(self):
        result = [unit() for unit in self.units]
        return "\n".join(result)

    def __mul__(self, other):
        if isinstance(other, int):
            return BoostedSystem(self.units, other)
        return NotImplemented


class BoostedUnit:
    def __init__(self, unit, factor):
        self.unit = unit
        self.factor = factor

    def __call__(self):
        if self.unit.energy > 0:
            self.unit.energy -= 10
            return f"{self.unit.name} SYSTEM ATTACK x{self.factor}!"
        return f"{self.unit.name} out of energy!"

    def __len__(self):
        return self.unit.energy

    def __bool__(self):
        return bool(self.unit)


class BoostedSystem:
    def __init__(self, units, factor):
        self.units = units
        self.factor = factor

    def __call__(self):
        result = []

        for unit in self.units:
            if unit.energy > 0:
                unit.energy -= 10
                result.append(f"{unit.name} SYSTEM ATTACK x{self.factor}!")
            else:
                result.append(f"{unit.name} out of energy!")

        return "\n".join(result)

    def __len__(self):
        return sum(unit.energy for unit in self.units)

    def __bool__(self):
        return any(bool(unit) for unit in self.units)


a2 = YoRHaUnit("A2", energy=100, damage=10)
b2 = YoRHaUnit("B2", energy=80, damage=12)

system = a2 + b2
boosted = system * 2

print(boosted())
print(len(a2))
print(bool(a2))
print(a2)
