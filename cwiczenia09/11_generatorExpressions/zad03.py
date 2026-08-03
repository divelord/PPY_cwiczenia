"""
ZAD03

Dla listy napisów oblicz łączną długość wszystkich napisów zaczynających się na literę "a",
używając generator expression.
"""

lst = ["asd", "fdg", "asdv", "dsvc", "a", "ad"]
gen = sum(len(x) for x in lst if x.startswith("a"))

print(gen)
