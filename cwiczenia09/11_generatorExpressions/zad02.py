"""
ZAD02

Mając listę liczb, użyj generator expression, aby policzyć, ile z nich jest większych od 5
(bez tworzenia dodatkowej listy).
"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gen = sum(1 for x in lst if x > 5)

print(gen)
