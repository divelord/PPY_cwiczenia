"""
ZAD01

Używając generator expression oraz funkcji sum, oblicz sumę kwadratów liczb od 1 do 10.
"""

gen = sum(x ** 2 for x in range(1, 11))

print(gen)
