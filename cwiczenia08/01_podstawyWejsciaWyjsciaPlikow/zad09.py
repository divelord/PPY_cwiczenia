"""
ZAD09

Znajdź wszystkie zdania zawierające słowo "ring" (bez uwzględniania wielkości liter) i wypisz je.
"""

with open("../THE_HOBBIT.txt", "r", encoding="utf-8") as file:
    text = file.read().replace("\n", " ").split(".")

    for line in text:
        words = line.lower().strip().split()

        if any(word.strip(",!?;:()\"'") == "ring" for word in words):
            print(line)
