"""
ZAD05

Znajdź najdłuższe słowo w tekście bez tworzenia listy słów.
"""


def find_longest_word(text):
    word = ""

    for ch in text:
        if ch != " ":
            word += ch
        elif word:
            yield word
            word = ""
    if word:
        yield word


text = "a bb dddd aaaaaaaaaa ccc eeeee ffffff"
longest_word = ""

for word in find_longest_word(text):
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)
