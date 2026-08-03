"""
ZAD02

Dla listy napisów utwórz zbiór pierwszych liter tych napisów.
"""

lst = ["asfg", "sfgd", "fdb", "aerwtgtbg", "sadfg", "hbgf"]
st = {el[0] for el in lst}
print(st)
