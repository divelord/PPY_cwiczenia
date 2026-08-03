"""
ZAD01

Używając list comprehension, utwórz listę kwadratów liczb z zakresu 1–10,
ale tylko dla liczb nieparzystych.
"""

lst = [x * x for x in range(1, 11) if x % 2 != 0]
print(lst)
