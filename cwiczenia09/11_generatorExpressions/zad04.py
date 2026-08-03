"""
ZAD04

Używając generator expression oraz funkcji any, sprawdź, czy w liście liczb istnieje liczba ujemna.
"""

lst = [3, 4, -5, 6, 7]
gen = any(x < 0 for x in lst)

print(gen)
