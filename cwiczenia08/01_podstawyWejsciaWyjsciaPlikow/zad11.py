"""
ZAD11

Podziel plik na rozdziały (przyjmij, że rozdziały zaczynają się od słowa "Chapter").
Policz, ile jest rozdziałów.
"""

with open("../THE_HOBBIT.txt", "r", encoding="utf-8") as file:
    text = file.read()

chapters = text.split("\nChapter")[1:]

print(len(chapters))
