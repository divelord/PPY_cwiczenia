"""
ZAD01

Utwórz:
a = 5
b = 9
Zamień wartości:
• najpierw klasycznie (z użyciem zmiennej pomocniczej),
• potem „krotkowo”
"""

a = 5
b = 9
print(a, b)

tmp = a
a = b
b = tmp
print(a, b)

a, b = b, a
print(a, b)
