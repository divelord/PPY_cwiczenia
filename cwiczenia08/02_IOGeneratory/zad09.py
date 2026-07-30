"""
ZAD09

Napisz generator, który zwraca zdania (przyjmij, że zdania kończą się kropką).
"""


def get_sentences(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        sentence = ""

        for line in file:
            word_lst = line.split()

            for word in word_lst:
                if not sentence:
                    sentence = word
                else:
                    sentence += " " + word

                if word.endswith("."):
                    yield sentence
                    sentence = ""


for sen in get_sentences("../THE_HOBBIT.txt"):
    print(sen)
