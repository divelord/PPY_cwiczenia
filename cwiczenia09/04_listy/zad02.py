"""
ZAD02

Dla listy napisów utwórz nową listę zawierającą tylko te napisy,
które są palindromami.
"""


def find_palindromes(lst):
    new_list = []

    for word in lst:
        if word == word[::-1]:
            new_list.append(word)

    return new_list


lst = ["aaa", "aba", "asd", "asb"]

print(find_palindromes(lst))
