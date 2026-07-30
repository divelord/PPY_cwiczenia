"""
ZAD12

Dla każdego rozdziału policz, ile razy pojawia się słowo "Bilbo".
"""

with open("../THE_HOBBIT.txt", "r", encoding="utf-8") as file:
    text = file.read()

chapters = text.split("\nChapter")[1:]
chapter_num = 0
word_to_count = "Bilbo"

for chapter in chapters:
    chapter_num += 1
    word_count = chapter.count(word_to_count)

    print(f"Chapter {chapter_num}: {word_count}")
