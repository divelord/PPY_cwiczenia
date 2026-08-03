"""
ZAD04

Napisz funkcję, która dla listy elementów zwraca listę bez duplikatów,
zachowując kolejność pierwszego wystąpienia elementów.
"""


def get_unique_elements(lst):
    st = set()
    result = []

    for el in lst:
        if el not in st:
            st.add(el)
            result.append(el)

    return result


lst = ["xzcvb", "asdfg", "werty", "xcvb", "utrdcfvgh", "werty"]

print(get_unique_elements(lst))
