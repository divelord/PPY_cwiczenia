"""
ZAD13

Znajdź rozdział z największą liczbą wystąpień słowa "dragon".
"""

with open("../THE_HOBBIT.txt", "r", encoding="utf-8") as file:
    content = file.read()

chapters = content.split("\nChapter")[1:]
chapter_num = 0
chapter_max_count = float("-inf")
chapter_with_max_count = None
word_to_find = "dragon"

for chapter in chapters:
    chapter_num += 1
    word_count = chapter.count(word_to_find)

    if word_count > chapter_max_count:
        chapter_max_count = word_count
        chapter_with_max_count = chapter_num

print(f"Chapter: {chapter_with_max_count}")
