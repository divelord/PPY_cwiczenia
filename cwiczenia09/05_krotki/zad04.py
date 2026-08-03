"""
ZAD04

Wyjaśnij, dlaczego poniższy kod działa lub nie działa, oraz jaki będzie jego wynik:
    t = (1, [2, 3])
    t[1].append(4)
"""

t = (1, [2, 3])
print(t)
t[1].append(4)
print(t)

'''Kod się powiedzie, ponieważ nie modyfikujemy samej krotki, tylko listę znajdującą się w tej krotce.'''
