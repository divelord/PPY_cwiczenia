"""
ZAD02

Dla listy krotek (liczba, napis) utwórz listę napisów posortowaną według liczb rosnąco.
"""


def sort_by_number(lst):
    sorted_lst = sorted(lst, key=lambda x: x[0])

    return [text for num, text in sorted_lst]


lst = [(5, "av"), (2, "cvb"), (8, "adsf")]

print(sort_by_number(lst))
