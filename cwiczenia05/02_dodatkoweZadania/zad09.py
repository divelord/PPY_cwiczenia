"""
ZAD09

Napisz generator, który przyjmuje listę i zwraca elementy wraz z ich indeksami:
[’a’,’b’,’c’] -> (0,’a’), (1,’b’), (2,’c’)
(nie używaj enumerate)
"""


def get_ind_el(lst):
    ind = 0

    for el in lst:
        yield ind, el
        ind += 1


lst = ["a", "b", "c"]
for i in get_ind_el(lst):
    print(i)
