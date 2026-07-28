"""
ZAD08

Napisz generator, który zwraca iloczyny skumulowane:
[1,2,3,4] -> 1, 2, 6, 24
"""


def cumulate(lst):
    result = 1

    for el in lst:
        result *= el
        yield result


lst = [1, 2, 3, 4]
for i in cumulate(lst):
    print(i)
