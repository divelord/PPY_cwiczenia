"""
ZAD05

Napisz funkcję, która:
• przyjmuje listę słów,
• zwraca słownik, w którym wartościami są listy anagramów.
Z otrzymanego słownika wypisz najdłuższą listę anagramów.
"""


def anagramy(lst):
    anagram = {}

    for i in lst:
        key = tuple(sorted(i))

        if key not in anagram:
            anagram[key] = []
        anagram[key].append(i)

    return anagram


words = ["ekran", "nerka", "mors", "szrom", "ranek"]
anagrams = anagramy(words)

print(max(anagrams.values(), key=len))
