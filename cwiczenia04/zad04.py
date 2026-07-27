"""
ZAD04

Oblicz sumę kwadratów liczb od 1 do 1 000 000 bez tworzenia listy.
Użyj generator expression.
"""

total_sum = sum(x ** 2 for x in range(1, 1000001))
print(total_sum)
