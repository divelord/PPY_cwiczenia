"""
ZAD13

Zaimplementuj własną wersję itertools.groupby, która grupuje kolejne identyczne słowa w tekście.
"""


def get_words(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            word_lst = line.split()
            for word in word_lst:
                yield word.lower()


def my_group_by(iterable):
    it = iter(iterable)

    try:
        previous = next(it)
    except StopIteration:
        return

    group = [previous]

    for word in it:
        if word == previous:
            group.append(word)
        else:
            yield previous, group
            previous = word
            group = [previous]

    yield previous, group


for word, group in my_group_by(get_words("../THE_HOBBIT.txt")):
    if len(group) > 1:
        print(word, group)
