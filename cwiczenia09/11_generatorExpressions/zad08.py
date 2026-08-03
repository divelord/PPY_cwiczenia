"""
ZAD08

Użyj generator expression, aby utworzyć napis, będący połączeniem wszystkich znaków z listy znaków
(użyj funkcji join).
"""

lst = ["asdvf", "sdsvf", "sdfvg", "dfg", "dfgb"]
gen = (" ".join(x for x in lst))

print(gen)
