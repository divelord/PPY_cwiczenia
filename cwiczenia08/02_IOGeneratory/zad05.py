"""
ZAD05

Utwórz generator words(file_path), który zwraca pojedyncze słowa z pliku.
"""


def words(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            word_lst = line.split()
            for word in word_lst:
                yield word


gen = words("../THE_HOBBIT.txt")

for word in range(100):
    print(next(gen))
