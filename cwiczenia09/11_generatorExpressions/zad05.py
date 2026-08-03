"""
ZAD05

Używając generator expression oraz funkcji all, sprawdź, czy wszystkie liczby w liście są parzyste.
"""

lst = [2, 4, 6, 8]
gen = all(x % 2 == 0 for x in lst)

print(gen)
