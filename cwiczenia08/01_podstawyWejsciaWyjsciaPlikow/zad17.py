"""
ZAD17

Znajdź wszystkie imiona postaci (przyjmij, że są to słowa pisane wielką literą,
które nie znajdują się na początku zdania) i policz ich wystąpienia.
"""

with open("../THE_HOBBIT.txt", "r", encoding="utf-8") as file:
    words = file.read().strip().split()

word_dct = {}
sentence_start = True

for word in words:
    clean_word = word.strip(".,!?;:()\"'")

    if clean_word:
        if clean_word[0].isupper() and not sentence_start:
            if clean_word not in word_dct:
                word_dct[clean_word] = 0
            word_dct[clean_word] += 1

        if word.endswith(".") or word.endswith("?") or word.endswith("!"):
            sentence_start = True
        else:
            sentence_start = False

print(sorted(word_dct.items(), key=lambda x: x[1], reverse=True))
