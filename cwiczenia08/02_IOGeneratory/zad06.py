"""
ZAD06

Użyj generatora słów, aby policzyć, ile razy pojawia się słowo "Bilbo".
"""


def count_word(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            word_lst = line.split()
            for word in word_lst:
                yield word


word_to_find = "Bilbo"
word_count = 0

for word in count_word("../THE_HOBBIT.txt"):
    if word == word_to_find:
        word_count += 1

print(word_count)
