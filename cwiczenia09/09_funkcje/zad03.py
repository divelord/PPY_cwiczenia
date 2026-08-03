"""
ZAD03

Wyjaśnij na przykładzie, czym różni się przekazanie listy jako argumentu od przekazania jej kopii.
"""


def add_to_list(lst):
    lst.append(4)


print("Przekazanie listy jako argument (referencja)")
lst_ref = [1, 2, 3]
print(lst_ref)
add_to_list(lst_ref)
print(lst_ref)

print("Przekazanie kopii listy")
lst_copy = [1, 2, 3]
print(lst_copy)
add_to_list(lst_copy[:])
print(lst_copy)
