"""
ZAD05

Zmodyfikuj poprzednie zadanie tak, aby zliczać wystąpienia "Bilbo" bez uwzględniania wielkości liter.
"""

with open("../THE_HOBBIT.txt", "r", encoding="utf-8") as file:
    words = file.read().lower().strip().split()

word_to_find = "bilbo"
print(words.count(word_to_find))
