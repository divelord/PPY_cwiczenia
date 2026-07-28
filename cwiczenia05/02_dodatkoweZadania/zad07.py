"""
ZAD07

Napisz generator, który przyjmuje napis i zwraca kolejne słowa (rozdzielone spacjami), bez użycia split().
"""


def split_text(text):
    word = ""

    for ch in text:
        if ch == " ":
            if word:
                yield word
                word = ""
        else:
            word += ch

    if word:
        yield word


text = "ab cde fgh ijk"
for i in split_text(text):
    print(i)
