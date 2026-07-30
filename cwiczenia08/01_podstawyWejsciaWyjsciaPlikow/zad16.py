"""
ZAD16

Zbuduj prostą konkordancję: dla każdego wystąpienia słowa "Bilbo"
wypisz to słowo wraz z trzema słowami przed nim i trzema po nim.
"""

with open("../THE_HOBBIT.txt", "r", encoding="utf-8") as file:
    words = file.read().strip().split()

concordance = "Bilbo"

for word in range(len(words)):
    if words[word] == concordance:
        start = max(0, word - 3)
        end = word + 4
        text = words[start:end]

        print(" ".join(text))
