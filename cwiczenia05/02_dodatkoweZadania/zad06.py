"""
ZAD06

Napisz generator, który przyjmuje listę i zwraca tylko unikalne elementy (z zachowaniem kolejności).
"""


def unique(lst):
    seen_element = []

    for el in lst:
        if el not in seen_element:
            yield el
            seen_element.append(el)


lst = [4, 1, 5, 2, 2, 3, 1, 4, 5, 2]
for i in unique(lst):
    print(i)
