"""
ZAD09

Mając listę list liczb, użyj generator expression, aby obliczyć sumę wszystkich elementów
we wszystkich listach (bez użycia zagnieżdżonych pętli jawnych).
"""

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
gen = sum(x for sub_list in lst for x in sub_list)

print(gen)
