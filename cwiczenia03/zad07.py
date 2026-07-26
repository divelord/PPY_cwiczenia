"""
ZAD07

Mając zdefiniowany słownik, gdzie kluczami są imiona osób,
a wartościami liczby zwycięstw danej osoby w turnieju szachowym,
stwórz nowy słownik, w którym kluczami są liczby zwycięstw,
a wartościami listy osób z taką liczbą zwycięstw.
Program powinien:
• utworzyć słownik liczba_zwyciestw → lista_osob,
• wydrukować wynik w czytelnej formie.
Następnie program powinien:
• utworzyć listę krotek (liczba_zwycięstw, lista_osób),
• posortować tę listę malejąco według liczby zwycięstw,
• wydrukować wynik.
"""

dct = {"John": 3, "Bill": 4, "Jane": 4, "Kim": 2, "Mary": 3, "Joe": 0, "Sue": 5, "Ada": 2, "Ray": 2}

victory_count = {}

for key, value in dct.items():
    if value not in victory_count:
        victory_count[value] = []
    victory_count[value].append(key)

print(victory_count)

tuple_list = []
for key, value in victory_count.items():
    tuple_list.append((key, tuple(value)))
tuple_list.sort(key=lambda x: x[0], reverse=True)

print(tuple_list)
