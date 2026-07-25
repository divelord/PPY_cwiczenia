"""
ZAD01

Utwórz:
x = 10
print(id(x))
x = x+1
print(id(x))
Czy id się zmieniło?
Co to oznacza?
"""

x = 10
print(id(x))
x = x + 1
print(id(x))
# Przy każdym nowym przypisaniu, zmienna wskazuje na inne miejsce w pamięci
