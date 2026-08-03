"""
ZAD03

Mając listę napisów, utwórz listę długości tych napisów, ale tylko dla tych,
które zaczynają się na literę "a".
"""

lst1 = ["asd", "dfg", "asada", "gbf", "asdg"]
lst2 = [len(el) for el in lst1 if el.startswith("a")]
print(lst2)
