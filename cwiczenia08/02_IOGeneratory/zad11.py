"""
ZAD11

Napisz generator, który w sposób leniwy (bez wczytywania całego pliku do pamięci)
zwraca pary (słowo, liczność).
"""


def get_word_with_count(file_path):
    word_dct = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            word_lst = line.lower().split()

            for word in word_lst:
                if word not in word_dct:
                    word_dct[word] = 0
                word_dct[word] += 1

                yield word, word_dct[word]


gen = get_word_with_count("../THE_HOBBIT.txt")

for word in range(100):
    print(next(gen))
