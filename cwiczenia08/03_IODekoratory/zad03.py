"""
ZAD03

Kronika Bilba
Twoim zadaniem jest analiza podróży Bilba zapisanej w pliku hobbit.txt.
Napisz dekorator chapter_reader, który przekształca funkcję w generator
przetwarzający książkę rozdział po rozdziale.
Założenia:
• Rozdziały zaczynają się od słowa "Chapter"
Dekorator powinien:
• czytać plik w sposób leniwy
• grupować linie w rozdziały
• zwracać kolejne rozdziały jako łańcuchy znaków
Użyj tego dekoratora na funkcji, która:
• zlicza, ile razy słowo "Bilbo" pojawia się w każdym rozdziale
Wypisz numer rozdziału oraz wynik.
"""


def chapter_reader(func):
    def wrapper(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            chapter = ""

            for line in file:
                if line.startswith("Chapter"):
                    if chapter and chapter.startswith("Chapter"):
                        yield func(chapter)
                    chapter = line
                else:
                    chapter += line

            if chapter and chapter.startswith("Chapter"):
                yield func(chapter)

    return wrapper


@chapter_reader
def word_count_for_chapter(chapter):
    return chapter.count("Bilbo")


chapter_gen = word_count_for_chapter("../THE_HOBBIT.txt")
chapter_num = 0

for count in chapter_gen:
    chapter_num += 1
    print(f"{chapter_num}: {count}")
