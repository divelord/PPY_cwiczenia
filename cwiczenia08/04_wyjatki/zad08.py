"""
ZAD08

Połącz wyjątki i generatory:
Napisz funkcję, która przetwarza plik w sposób leniwy i zgłasza wyjątek,
jeśli nie zostanie znalezione żadne imię postaci (słowo zapisane wielką literą).
"""
from exceptions import NoNameException


def check_for_characters(path):
    found = False

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            word_lst = line.split()
            for word in word_lst:
                clean_word = word.strip(".,!?;:()\"'")
                if clean_word:
                    if clean_word[0].isupper():
                        found = True
                    yield clean_word

    if not found:
        raise NoNameException("Brak imienia postaci")


try:
    for name in check_for_characters("../THE_HOBBIT.txt"):
        pass
except NoNameException as e:
    print(e)
