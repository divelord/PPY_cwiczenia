"""
ZAD06

Użyj generator expression, aby znaleźć maksymalną długość napisu w liście napisów.
"""

lst = ["sdf", "fghj", "cvbikuli", "jyktfug"]
gen = max(len(x) for x in lst)

print(gen)
