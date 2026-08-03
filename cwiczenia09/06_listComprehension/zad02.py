"""
ZAD02

Dla listy liczb stwórz nową listę, w której liczby ujemne zostaną zastąpione
ich wartością bezwzględną.
"""

lst1 = [1, -1, 2, 3, 4, -5, -10]
lst2 = [abs(num) for num in lst1]
print(lst2)
