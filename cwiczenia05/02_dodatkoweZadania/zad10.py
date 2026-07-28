"""
ZAD10

Napisz generator spłaszczający listę zagnieżdżoną (jeden poziom):
[[1,2],[3,4],[5]] -> 1,2,3,4,5
"""


def flatten_list(lst):
    for sub_lst in lst:
        for el in sub_lst:
            yield el


nested_lst = [[1, 2], [3, 4], [5]]
for i in flatten_list(nested_lst):
    print(i)
