"""
ZAD08

Utwórz potok generatorów:
• pierwszy generator: zwraca linie
• drugi generator: dzieli linie na słowa
• trzeci generator: filtruje słowa (np. dłuższe niż 4 znaki)
"""


def get_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()


def get_words(lines):
    for line in lines:
        word_lst = line.split()
        for word in word_lst:
            yield word


def filter_words(words, length):
    for word in words:
        if len(word) > length:
            yield word


gen_lines = get_lines("../THE_HOBBIT.txt")
gen_words = get_words(gen_lines)
gen_filter = filter_words(gen_words, 4)

for word in range(10):
    print(next(gen_filter))
