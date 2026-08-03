"""
ZAD02

Dany jest słownik, w którym wartościami są listy liczb.
Utwórz set wszystkich liczb większych od 5 występujących w tych listach.
"""


def filter_numbers(dct):
    st = set()

    for k, v in dct.items():
        for i in v:
            if i > 5:
                st.add(i)

    return st


dct = {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}

print(filter_numbers(dct))
