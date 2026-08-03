"""
ZAD01

Mając listę krotek (imię, wiek), znajdź krotkę z największym wiekiem.
"""


def find_oldest_person(lst):
    return max(lst, key=lambda x: x[1])


lst = [("A", 10), ("B", 15), ("C", 13)]

print(find_oldest_person(lst))
