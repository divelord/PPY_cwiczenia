"""
ZAD07

Mając listę liczb, utwórz generator expression, który zwraca tylko liczby podzielne przez 3,
a następnie wypisz je w pętli.
"""

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gen = (x for x in lst if x % 3 == 0)

for i in gen:
    print(i)
