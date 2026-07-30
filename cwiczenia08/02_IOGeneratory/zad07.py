"""
ZAD07

Napisz generator, który zwraca tylko słowa dłuższe niż 5 znaków.
"""


def get_words_longer_than_5(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            word_lst = line.split()
            for word in word_lst:
                if len(word) > 5:
                    yield word


gen = get_words_longer_than_5("../THE_HOBBIT.txt")

for word in range(10):
    print(next(gen))
