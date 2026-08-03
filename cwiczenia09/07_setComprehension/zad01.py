"""
ZAD01

Utwórz zbiór wszystkich reszt z dzielenia liczb od 1 do 20 przez 3.
"""

st = {x % 3 for x in range(1, 21)}
print(st)
