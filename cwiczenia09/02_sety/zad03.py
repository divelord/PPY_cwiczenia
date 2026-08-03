"""
ZAD03

Mając listę liczb całkowitych, sprawdź, czy zawiera ona duplikaty,
wykorzystując zbiór. Zwróć True lub False.
"""


def has_duplicates(lst):
    return len(lst) != len(set(lst))


lst1 = [1, 2, 3, 4, 1]
lst2 = [1, 2, 3, 4, 5]

print(has_duplicates(lst1))
print(has_duplicates(lst2))
