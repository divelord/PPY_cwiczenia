"""
ZAD24

Program definiuje dwie listy: lsta i lstb. Utwórz i wypisz dwie listy:
• jedną zawierającą wszystkie elementy bez powtórzeń (suma zbiorów),
• jedną zawierającą elementy wspólne (część wspólna), również bez powtórzeń.
"""

lsta = [1, 2, 3, 4, 5, 6]
lstb = [5, 6, 7, 8, 9, 10]

seta = set(lsta)
setb = set(lstb)

union_lst = list(seta.union(setb))
intersection_lst = list(seta.intersection(setb))

print(union_lst)
print(intersection_lst)
